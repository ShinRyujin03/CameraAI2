from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from schema import SchemaError
from app.sevices.face_functions import FaceLocationDetection,FaceLandmarksDetection
from database.database import Database
face_router = Blueprint('face_router', __name__)

# Create instances of the function classes
face_detector = FaceLocationDetection()
landmarks_detector = FaceLandmarksDetection()


# Route for face landmarks
@face_router.route('/face_landmarks', methods=['POST'])
def get_face_landmarks():
    try:
        image_file = request.files['image']  # Access the uploaded file
        if image_file:
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
            return jsonify(result, {"message": f"Face landmark metadata of {image_name} saved successfully"})

        else:
            return jsonify({'error': 'No image file uploaded'}), 400
    except SchemaError as e:
        error_msg = str(e)
        return jsonify({'error': error_msg}), 400

# Route for face location
@face_router.route('/face_location', methods=['POST'])
def get_face_location():
    try:
        image_file = request.files['image']  # Access the uploaded file
        if image_file:
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
            db.insert_face_location(image_name, face_locations)
            db.close_connection()
            return jsonify(result, {"message": f"Face location metadata of {image_name} saved successfully"})
        else:
            return jsonify({'error': 'No image file uploaded'}), 400
    except SchemaError as e:
        error_msg = str(e)
        return jsonify({'error': error_msg}), 400