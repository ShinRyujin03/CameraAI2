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

class EmotionRecognition:
    def __init__(self):
        self.image_data = None

    def emotions_recognition(self):
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        # Phân tích cảm xúc bằng DeepFace
        emotions_data = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False)

        emotions_list = []
        emotion_weights_list = []

        for face in emotions_data:
            dominant_emotion = face['dominant_emotion']
            emotion_weight = max(face['emotion'].values())

            emotions_list.append(dominant_emotion)
            emotion_weights_list.append(round(emotion_weight,3))

        return emotions_list, emotion_weights_list

    def get_emotions_recognition(self, image_file):
        emotions_detector = EmotionRecognition()
        if schema_test(image_file):
            try:
                # Read the image data from the file
                image_name = secure_filename(image_file.filename)
                logging.info(f'image_name: {image_name}')

                # Process the image using emotions_detector
                emotions_detector.image_data = image_data
                emotions, emotion_weights = emotions_detector.emotions_recognition()

                # Get face locations using face_detector
                face_detector = FaceLocationDetection()
                face_detector.image_data = image_data
                face_locations = face_detector.facelocation()

                # Create a response object
                result = {
                    'image_name': image_name,
                    'face_locations': face_locations,
                    'emotions': emotions,
                    'emotion_weight': emotion_weights,
                }

                if not face_locations:  # Check if no face locations were detected
                    logging.error(NoDetection())
                    raise NoDetection

                db = Database()
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                if len(str(face_locations)) > 500:
                    logging.error(OutputTooLongError())
                    raise OutputTooLongError
                else:
                    db.insert_face_emotions(image_name, face_locations, emotions, emotion_weights)
                    db.insert_image_file(image_name, image_data)
                    db.close_connection()
                    logging.info(result, {"message": f"Face emotions metadata of {image_name} saved successfully"})
                    return jsonify(result, {"message": f"Face emotions metadata of {image_name} saved successfully"})