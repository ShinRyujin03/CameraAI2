import mysql
from flask import jsonify
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from ultralytics import YOLO
from database.database import Database
from app.schema.image_schema import *
from app.handle.app_error import DatabaseNoneError, NoDetection, OutputTooLongError
import configparser
import logging
import base64

# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")

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
        results = model(image)  # results list
        detected_boxes = []
        detected_weights = []
        # Filter results based on the condition r.boxes.cls[i] == 0
        for r in results:
            cls_values = r.boxes.cls.tolist()  # Convert tensor to list
            for i, cls in enumerate(cls_values):
                if cls == config.getint('human_detection_config', 'label_class'):  # Only consider when cls is equal to 'label_class'
                    rounded_boxes = [round(value, config.getint('human_detection_config', 'round_result')) for value in r.boxes.xywh[i].tolist()]
                    detected_boxes.append(rounded_boxes)
                    detected_weights.append(round(r.boxes.conf[i].item(), config.getint('human_detection_config', 'round_result')))  # Use .item() to convert scalar tensor to Python number
        return detected_boxes, detected_weights
    def get_human_location(self, image_file):
        human_detector = HumanDetection()
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                base64_image = base64.b64encode(image_data)
                base64_image_string = base64_image.decode('utf-8')
                image_name = secure_filename(image_file.filename)
                logging.info(f'image_name: {image_name}')
                # Process the image using human_detector
                human_detector.image_data = image_data
                detected_boxes, detected_weights = human_detector.humanlocation()

                # You can return the results as needed
                result = {
                    'detections': [{'box': box, 'weight': weight} for box, weight in
                                   zip(detected_boxes, detected_weights)],
                    'image_name': image_name
                }
                if len(detected_boxes) == 0:
                    logging.error(NoDetection())
                    raise NoDetection
                db = Database()
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                if len(detected_boxes) > 500:
                    logging.error(OutputTooLongError())
                    raise OutputTooLongError
                else:
                    db.insert_human_location(image_name, detected_boxes, detected_weights)
                    db.insert_image_file(image_name, base64_image_string)
                    db.close_connection()
                    logging.info(result, {"message": f"Human location metadata of {image_name} saved successfully"})
                    return jsonify(result, {"message": f"Human location metadata of {image_name} saved successfully"})