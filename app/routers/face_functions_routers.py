from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from app.sevices.face_functions import FaceLocationDetection,FaceLandmarksDetection
from app.handle.app_error import InvalidImageError, NoImageError,DatabaseNoneError
from database.database import Database
import os
from app.config.face_functions_config import Face_config
# Create instances of the function classes

face_router = Blueprint('face_router', __name__)
face_detector = FaceLocationDetection()
landmarks_detector = FaceLandmarksDetection()


# Route for face landmarks
@face_router.route('/face_landmarks', methods=['POST'])
def get_face_landmarks():
    image_file = request.files['image']  # Access the uploaded file
    if not image_file:
        raise NoImageError

    # Check if the uploaded file has a valid image extension
    allowed_extensions = Face_config.path
    filename, extension = os.path.splitext(image_file.filename)
    if extension[1:].lower() not in allowed_extensions:
        raise InvalidImageError
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


# Route for face location
@face_router.route('/face_location', methods=['POST'])
def get_face_location():
    image_file = request.files['image']  # Access the uploaded file
    if not image_file:
        raise NoImageError

    # Check if the uploaded file has a valid image extension
    allowed_extensions = Face_config.path
    filename, extension = os.path.splitext(image_file.filename)
    if extension[1:].lower() not in allowed_extensions:
        raise InvalidImageError
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
        return jsonify(result,{"message": f"Face location metadata of {image_name} saved successfully"})

