from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename

from app.functions.human_detection import HumanDetection
from app.functions.face_location import FaceLocationDetection
from app.functions.face_landmarks import FaceLandmarksDetection
from database.database import Database
functions_router = Blueprint('functions_router', __name__)

# Create instances of the function classes
human_detector = HumanDetection()
face_detector = FaceLocationDetection()
landmarks_detector = FaceLandmarksDetection()

# Route for human location
@functions_router.route('/human_location', methods=['POST'])
def get_human_location():
    image_file = request.files['image']  # Access the uploaded file
    if image_file:
        # Read the image data from the file
        image_data = image_file.read()
        image_name = secure_filename(image_file.filename)
        # Process the image using human_detector
        human_detector.image_data = image_data
        detected_boxes, detected_weights = human_detector.humanlocation()

        # You can return the results as needed
        result = {
            'image_name': image_name,
            'detections': [{'box': box, 'weight': weight} for box, weight in
                           zip(detected_boxes, detected_weights)]
        }
        db = Database()
        db.insert_human_location(image_name, detected_boxes, detected_weights)
        db.close_connection()
        return jsonify(result, {"message": f"Human location metadata of {image_name} saved successfully"})
    else:
        return jsonify({'error': 'No image file uploaded'}), 400



# Route for face landmarks
@functions_router.route('/face_landmarks', methods=['POST'])
def get_face_landmarks():
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
        return jsonify(result,{"message": f"Face landmark metadata of {image_name} saved successfully"})

    else:
        return jsonify({'error': 'No image file uploaded'}), 400

# Route for face location
@functions_router.route('/face_location', methods=['POST'])
def get_face_location():
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
