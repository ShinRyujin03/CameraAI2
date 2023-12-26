import logging

from flask import Blueprint, request, jsonify

from app.handle.app_error import FileUnreachable
from app.services.face.face_detection_services import FaceLocationDetection
from app.services.face.face_landmarks_sevices import FaceLandmarksDetection
from app.services.face.face_recognition_services import NameRecognition
from app.services.face.face_verification_services import FaceVerification
from app.services.face.facial_attribute_recognition_services import FacialAttributeRecognition

# Create instances of the function classes
face_router = Blueprint('face_router', __name__)


@face_router.route('/face_location', methods=['POST'])
def request_face_location():
    try:
        image_files = request.files.getlist('image')  # Access the list of uploaded files
    except Exception:
        logging.error(FileUnreachable())
        raise FileUnreachable

    results = []

    face_detector = FaceLocationDetection()
    for image_file in image_files:
        face_result = face_detector.get_face_location(image_file)
        results.append(face_result)  # Extract JSON content from each response

    return jsonify([result.get_json() for result in results])


# Route for face landmarks
@face_router.route('/face_landmarks', methods=['POST'])
def request_face_landmarks():
    try:
        image_files = request.files.getlist('image')  # Access the list of uploaded files
    except Exception:
        logging.error(FileUnreachable())
        raise FileUnreachable

    results = []

    face_landmarks = FaceLandmarksDetection()
    for image_file in image_files:
        landmarks_result = face_landmarks.get_face_landmarks(image_file)
        results.append(landmarks_result)  # Extract JSON content from each response
    return jsonify([result.get_json() for result in results])


@face_router.route('/facial_attribute_recognition', methods=['POST'])
def request_facial_attribute_recognition():
    try:
        image_files = request.files.getlist('image')  # Access the list of uploaded files
    except Exception:
        logging.error(FileUnreachable())
        raise FileUnreachable

    results = []

    face_facial_attribute = FacialAttributeRecognition()
    for image_file in image_files:
        facial_attribute_result = face_facial_attribute.get_facial_attribute_recognition(image_file)
        results.append(facial_attribute_result)  # Extract JSON content from each response
    return jsonify([result.get_json() for result in results])


@face_router.route('/face_verify', methods=['POST'])
def request_face_verification():
    face_name = request.form['face_name']
    try:
        image_file = request.files['image']  # Access the uploaded file
    except Exception:
        logging.error(FileUnreachable())
        raise FileUnreachable
    face_verify = FaceVerification()
    face_verify_result = face_verify.get_face_verification(image_file, face_name)
    return face_verify_result


@face_router.route('/face_name_recognition', methods=['POST'])
def request_name_recognition():
    try:
        image_files = request.files.getlist('image')  # Access the list of uploaded files
    except Exception:
        logging.error(FileUnreachable())
        raise FileUnreachable

    name_recognition = NameRecognition()  # Create a single instance

    results = []

    for image_file in image_files:
        name_recognition_result = name_recognition.get_face_name_recognition(image_file)
        results.append(name_recognition_result)  # Append each response object

    return jsonify([result.get_json() for result in results])
