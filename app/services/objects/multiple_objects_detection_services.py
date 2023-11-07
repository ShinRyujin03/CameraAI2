import cv2
import mysql
import numpy as np
from flask import jsonify
from ultralytics import YOLO
from werkzeug.utils import secure_filename

from app.handle.app_error import DatabaseNoneError, NoDetection, OutputTooLongError
from app.schema.image_schema import *
from database.database import Database

# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")

# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)


class MultipleObjectDetection:
    def __init__(self):
        self.image_data = None

    def objectslocation(self):
        # Load a pretrained YOLOv8n model
        model = YOLO(config.get('objects_detection_config', 'model_path'))
        # Convert image data to numpy array
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        results = model(image)  # results list
        detected_boxes = []
        detected_weights = []
        detected_objects = []
        # Filter results based on the condition r.boxes.cls[i] == 0
        for r in results:
            cls_values = r.boxes.cls.tolist()  # Convert tensor to list
            names = {
                0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane',
                5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light',
                10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench',
                14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep',
                19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe',
                24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie',
                28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard',
                32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove',
                36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle',
                40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon',
                45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange',
                50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut',
                55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed',
                60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse',
                65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave',
                69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator',
                73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors',
                77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'
            }
            for i, cls in enumerate(cls_values):
                cls_name = names[round(cls, 0)]
                detected_objects.append(cls_name)
                rounded_boxes = [round(value, config.getint('objects_detection_config', 'round_result')) for value in
                                 r.boxes.xywh[i].tolist()]
                detected_boxes.append(rounded_boxes)
                detected_weights.append(round(r.boxes.conf[i].item(), config.getint('objects_detection_config',
                                                                                    'round_result')))  # Use .item() to convert scalar tensor to Python number
        return detected_objects, detected_boxes, detected_weights

    def get_objects_location(self, image_file):
        objects_detector = MultipleObjectDetection()
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                image_name = secure_filename(image_file.filename)
                logging.info(f'image_name: {image_name}')
                # Process the image using objects_detector
                objects_detector.image_data = image_data
                detected_objects, detected_boxes, detected_weights = objects_detector.objectslocation()
                # You can return the results as needed
                result = {
                    'detections': [{'object type': obj, 'box': box, 'weight': weight} for obj, box, weight in
                                   zip(detected_objects, detected_boxes, detected_weights)],
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
                if len(detected_boxes) > config.getint('db_limit_config', 'objects_detected_boxes'):
                    logging.error(OutputTooLongError())
                    raise OutputTooLongError
                else:
                    try:
                        db.insert_detected_objects(image_name, detected_objects, detected_boxes, detected_weights)
                        db.insert_image_file(image_name, image_data)
                        db.close_connection()
                        logging.info(result,
                                     {"message": f"Objects detection metadata of {image_name} saved successfully"})
                        return jsonify(result,
                                       {"message": f"Objects detection metadata of {image_name} saved successfully"})
                    except Exception as e:
                        return str(e)
