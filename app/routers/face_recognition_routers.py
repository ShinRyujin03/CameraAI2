from flask import Blueprint, request
from app.services.face_recognition_sevices import  FaceLandmarksDetection
# Create instances of the function classes
face_recognition_router = Blueprint('face_recognition_router', __name__)

# Route for face landmarks
@face_recognition_router.route('/face_landmarks', methods=['POST'])
def request_face_landmarks():
    image_file = request.files['image']  # Access the uploaded file
    face_landmarks = FaceLandmarksDetection()
    landmarks_result = face_landmarks.get_face_landmarks(image_file)
    return landmarks_result