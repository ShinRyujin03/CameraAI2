from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from app.camera_schema import *
from database.database import Database
import face_recognition
import cv2
import numpy as np
from app.handle.app_error import DatabaseNoneError
import os
from app.config.face_functions_config import Face_config
# Create instances of the function classes

face_router = Blueprint('face_router', __name__)

class FaceLocationDetection:
    def __init__(self):
        self.image_data = None

    def facelocation(self):
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        face_locations = face_recognition.face_locations(image)
        return face_locations
class FaceLandmarksDetection:
    def __init__(self):
        self.image_data = None

    def facelandmarks(self):
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        face_landmarks_list = face_recognition.face_landmarks(image)
        return face_landmarks_list
# Route for face location
@face_router.route('/face_location', methods=['POST'])
def get_face_location():
        face_detector = FaceLocationDetection()
        image_file = request.files['image']  # Access the uploaded file
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
                # Return the response before attempting database operations
                db = Database()
                db.insert_face_location(image_name, face_locations)
                db.close_connection()
            except:
                raise DatabaseNoneError
            else:
                return jsonify(result, {"message": f"Face location metadata of {image_name} saved successfully"})


# Route for face landmarks
@face_router.route('/face_landmarks', methods=['POST'])
def get_face_landmarks():
        landmarks_detector = FaceLandmarksDetection()
        image_file = request.files['image']  # Access the uploaded file
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
                db.insert_face_landmark(image_name, landmarks)
                db.close_connection()
            except:
                raise DatabaseNoneError
            else:
                return jsonify(result, {"message": f"Face metadata of {image_name} saved successfully"})

