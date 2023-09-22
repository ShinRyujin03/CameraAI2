from flask import Blueprint, request
from app.services.face_detection_services import FaceLocationDetection

# Create instances of the function classes
face_detection_router = Blueprint('face_detection_router', __name__)

# Route for face location
@face_detection_router.route('/face_location', methods=['POST'])
def request_face_location():
    image_file = request.files['image']  # Access the uploaded file
    face_detector = FaceLocationDetection()
    face_result = face_detector.get_face_location(image_file)
    return face_result
