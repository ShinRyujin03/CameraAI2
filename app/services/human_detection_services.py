from flask import jsonify
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from ultralytics import YOLO
from database.database import Database
from app.camera_schema import *
from app.handle.app_error import DatabaseNoneError, NoDetection
import configparser

# Get the current directory of your script
script_directory = os.path.dirname(os.path.realpath("config/config.ini"))

# Construct the relative path to config.ini
config_path = os.path.join(script_directory,'config.ini')

# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)
class HumanDetection:
    def __init__(self):
        self.image_data = None

    def humanlocation(self):
        # Load a pretrained YOLOv8n model
        model = YOLO(config.get('human_detection_config', 'model_path'))
        # Convert image data to numpy array
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        # Run inference on 'bus.jpg'
        results = model(image)  # results list
        detected_boxes = []
        detected_weights = []

        # Filter results based on the condition r.boxes.cls[i] == 0
        for r in results:
            cls_values = r.boxes.cls.tolist()  # Convert tensor to list
            for i, cls in enumerate(cls_values):
                if cls == config.getint('human_detection_config', 'label_class'):  # Only consider when cls is equal to 0
                    rounded_boxes = [round(value, config.getint('human_detection_config', 'round_result')) for value in r.boxes.xywh[i].tolist()]
                    detected_boxes.append(rounded_boxes)
                    detected_weights.append(
                        round(r.boxes.conf[i].item(), config.getint('human_detection_config', 'round_result')))  # Use .item() to convert scalar tensor to Python number

        return detected_boxes, detected_weights

    def get_human_location(self, image_file):
        human_detector = HumanDetection()
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                image_name = secure_filename(image_file.filename)

                # Process the image using human_detector
                human_detector.image_data = image_data
                detected_boxes, detected_weights = human_detector.humanlocation()

                # You can return the results as needed
                result = {
                    'image_name': image_name,
                    'detections': [{'box': box, 'weight': weight} for box, weight in
                                   zip(detected_boxes, detected_weights)]
                }
                db = Database()
            except:
                raise DatabaseNoneError()
            else:
                if len(detected_boxes) == 0:
                    raise NoDetection
                else:
                    db.insert_human_location(image_name, detected_boxes, detected_weights)
                    db.close_connection()
                    return jsonify(result, {"message": f"Human location metadata of {image_name} saved successfully"})