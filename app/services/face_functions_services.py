from flask import jsonify
from werkzeug.utils import secure_filename
from app.schema.image_schema import *
from database.database import Database
import face_recognition
import cv2
import numpy as np
from app.handle.app_error import DatabaseNoneError, NoDetection
class FaceLocationDetection:
    def __init__(self):
        self.image_data = None

    def facelocation(self):
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        face_locations = face_recognition.face_locations(image)
        return face_locations

    def get_face_location(self,image_file):
        face_detector = FaceLocationDetection()
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                image_name = secure_filename(image_file.filename)
                # Process the image using face_detector
                face_detector.image_data = image_data
                face_locations = face_detector.facelocation()
                # Create a response object
                result = {
                    'image_name': image_name,
                    'face_locations': face_locations
                }
                db = Database()
            except:
                raise DatabaseNoneError
            else:
                if len(face_locations) == 0:
                    raise NoDetection
                else:
                    db.insert_face_location(image_name, face_locations)
                    db.close_connection()
                    return jsonify(result, {"message": f"Face location metadata of {image_name} saved successfully"})
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
                # Process the image using landmarks_detector
                landmarks_detector.image_data = image_data
                landmarks = landmarks_detector.facelandmarks()

                # Create a response object
                result = {
                    'image_name': image_name,
                    'landmarks': landmarks
                }
                db = Database()
            except:
                raise DatabaseNoneError
            else:
                if len(landmarks) == 0:
                    raise NoDetection
                else:
                    db.insert_face_landmark(image_name, landmarks)
                    db.close_connection()
                    return jsonify(result, {"message": f"Face metadata of {image_name} saved successfully"})