import mysql
from flask import jsonify
import base64
import face_recognition
import cv2
import numpy as np
from deepface import DeepFace

from werkzeug.utils import secure_filename
from app.schema.image_schema import *
from database.database import Database
from app.handle.app_error import DatabaseNoneError, NoDetection, OutputTooLongError
from app.services.face_detection_services import FaceLocationDetection


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
                base64_image = base64.b64encode(image_data)
                base64_image_string = base64_image.decode('utf-8')
                image_name = secure_filename(image_file.filename)
                logging.info(f'image_name: {image_name}')
                # Process the image using landmarks_detector
                landmarks_detector.image_data = image_data
                landmarks = landmarks_detector.facelandmarks()
                # Create a response object
                result = {
                    'image_name': image_name,
                    'landmarks': landmarks
                }
                if len(landmarks) == 0:
                    logging.error(NoDetection())
                    raise NoDetection
                db = Database()
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                if len(landmarks[0]["bottom_lip"]) > 250:
                    logging.error(OutputTooLongError())
                    raise OutputTooLongError
                else:
                    db.insert_face_landmark(image_name, landmarks)
                    db.insert_image_file(image_name, base64_image_string)
                    db.close_connection()
                    logging.info(result, {"message": f"Face metadata of {image_name} saved successfully"})
                    return jsonify(result, {"message": f"Face metadata of {image_name} saved successfully"})

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
                image_data = image_file.read()
                base64_image = base64.b64encode(image_data)
                base64_image_string = base64_image.decode('utf-8')
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
                    db.insert_image_file(image_name, base64_image_string)
                    db.close_connection()
                    logging.info(result, {"message": f"Face emotions metadata of {image_name} saved successfully"})
                    return jsonify(result, {"message": f"Face emotions metadata of {image_name} saved successfully"})



