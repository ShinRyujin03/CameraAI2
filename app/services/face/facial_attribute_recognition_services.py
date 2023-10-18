import mysql
from flask import jsonify
import base64
import cv2
import numpy as np
from deepface import DeepFace

from werkzeug.utils import secure_filename
from app.schema.image_schema import *
from database.database import Database
from app.handle.app_error import DatabaseNoneError, NoDetection, OutputTooLongError
from app.services.face.face_detection_services import FaceLocationDetection
import configparser

# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")

# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)

class FacialAttributeRecognition:
    def __init__(self):
        self.image_data = None

    def facial_attribute_recognition(self):
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        # Phân tích cảm xúc bằng DeepFace
        emotions_data = DeepFace.analyze(image, actions=['emotion', 'age', 'gender'], enforce_detection=False, silent=True)

        emotions_list = []
        emotion_weights_list = []

        age_list = []
        gender_list = []

        for face in emotions_data:
            dominant_emotion = face['dominant_emotion']
            emotion_weight = max(face['emotion'].values())
            age_min = face['age'] - 9
            age_max = age_min + 5
            gender = max(face['gender'], key=face['gender'].get)

            emotions_list.append(dominant_emotion)
            emotion_weights_list.append(round(emotion_weight,3))

            age_list.append(f"{age_min} - {age_max}")
            gender_list.append(gender)

        return emotions_list, emotion_weights_list, age_list, gender_list

    def get_facial_attribute_recognition(self, image_file):
        emotions_detector = FacialAttributeRecognition()
        if schema_test(image_file):
            try:
                # Read the image data from the file
                image_data = image_file.read()
                image_name = secure_filename(image_file.filename)
                logging.info(f'image_name: {image_name}')

                try:
                    # Process the image using emotions_detector
                    emotions_detector.image_data = image_data
                    emotions, emotion_weights, age, gender = emotions_detector.facial_attribute_recognition()
                except Exception as e:
                    return str(e)

                # Create a response object
                result = {
                    'image_name': image_name,
                    'emotions': emotions,
                    'age' : age,
                    'gender': gender,
                }

                if not emotions:  # Check if no face locations were detected
                    logging.error(NoDetection())
                    raise NoDetection

                db = Database()
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                if len(str(emotions)) > config.getint('db_limit_config', 'emotions'):
                    logging.error(OutputTooLongError())
                    raise OutputTooLongError
                else:
                    try:
                        db.insert_face_facial_attubute(image_name, emotions, age, gender)
                        db.insert_image_file(image_name, image_data)
                        db.close_connection()
                        logging.info(result, {"message": f"Face emotions metadata of {image_name} saved successfully"})
                        return jsonify(result, {"message": f"Face emotions metadata of {image_name} saved successfully"})
                    except Exception as e:
                        return str(e)