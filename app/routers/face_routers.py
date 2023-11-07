from flask import Blueprint, request

from app.services.face.face_detection_services import FaceLocationDetection
from app.services.face.face_landmarks_sevices import FaceLandmarksDetection
from app.services.face.face_recognition_services import NameRecognition
from app.services.face.face_verification_services import FaceVerification
from app.services.face.facial_attribute_recognition_services import FacialAttributeRecognition

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


@face_router.route('/facial_attribute_recognition', methods=['POST'])
def request_facial_attribute_recognition():
    image_file = request.files['image']  # Access the uploaded file
    face_facial_attribute = FacialAttributeRecognition()
    facial_attribute_result = face_facial_attribute.get_facial_attribute_recognition(image_file)
    return facial_attribute_result


@face_router.route('/face_verify', methods=['POST'])
def request_face_verification():
    face_name = request.form['face_name']
    image_file = request.files['image']  # Access the uploaded file
    face_verify = FaceVerification()
    face_verify_result = face_verify.get_face_verification(image_file, face_name)
    return face_verify_result


@face_router.route('/face_name_recognition', methods=['POST'])
def request_name_recognition():
    image_file = request.files['image']  # Access the uploaded file
    name_recognition = NameRecognition()
    name_recognition_result = name_recognition.get_face_name_recognition(image_file)
    return name_recognition_result
