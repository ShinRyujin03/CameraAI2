import mysql
from flask import jsonify
import face_recognition
import cv2
import numpy as np

from werkzeug.utils import secure_filename
from app.schema.image_schema import *
from database.database import Database
from app.handle.app_error import DatabaseNoneError, NoDetection, OutputTooLongError


# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")

# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)
class FaceLandmarksDetection:
    def __init__(self):
        self.image_data = None
    def facelandmarks(self):
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        face_landmarks_list = face_recognition.face_landmarks(image)
        return face_landmarks_list
    def get_face_landmarks(self,image_file):
        landmarks_detector = FaceLandmarksDetection()
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                image_name = secure_filename(image_file.filename)
                logging.info(f'image_name: {image_name}')
                # Process the image using landmarks_detector
                landmarks_detector.image_data = image_data
                landmarks = landmarks_detector.facelandmarks()
                # Create a response object
                result = {
                    'landmarks': landmarks,
                    'image_name': image_name
                }
                if len(landmarks) == 0:
                    logging.error(NoDetection())
                    raise NoDetection
                db = Database()
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                if len(landmarks[0]["bottom_lip"]) > config.getint('db_limit_config', 'landmarks'):
                    logging.error(OutputTooLongError())
                    raise OutputTooLongError
                else:
                    try:
                        db.insert_face_landmark(image_name, landmarks)
                        db.insert_image_file(image_name, image_data)
                        db.close_connection()
                        logging.info(result, {"message": f"Face metadata of {image_name} saved successfully"})
                        return jsonify(result, {"message": f"Face metadata of {image_name} saved successfully"})
                    except Exception as e:
                        return str(e)