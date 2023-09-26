from flask import Blueprint, request
from app.services.face.face_landmarks_sevices import  FaceLandmarksDetection
from app.services.face.emotions_recognition_services import EmotionRecognition
from app.services.face.face_detection_services import FaceLocationDetection
# Create instances of the function classes
face_router = Blueprint('face_router', __name__)

# Route for face location
@face_router.route('/face_location', methods=['POST'])
def request_face_location():
    image_file = request.files['image']  # Access the uploaded file
    face_detector = FaceLocationDetection()
    face_result = face_detector.get_face_location(image_file)
    return face_result


# Route for face landmarks
@face_router.route('/face_landmarks', methods=['POST'])
def request_face_landmarks():
    image_file = request.files['image']  # Access the uploaded file
    face_landmarks = FaceLandmarksDetection()
    landmarks_result = face_landmarks.get_face_landmarks(image_file)
    return landmarks_result

@face_router.route('/emotions_recognition', methods=['POST'])
def request_emotions_recognition():
    image_file = request.files['image']  # Access the uploaded file
    face_emotions = EmotionRecognition()
    emotions_result = face_emotions.get_emotions_recognition(image_file)
    return emotions_result