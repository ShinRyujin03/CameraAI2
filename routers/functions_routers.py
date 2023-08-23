from flask import Blueprint, jsonify, request
from app.functions.human_detection import HumanDetection
from app.functions.face_location import FaceLocationDetection
from app.functions.face_landmarks import FaceLandmarksDetection
functions_router = Blueprint('functions_router', __name__)

# Create instances of the function classes
human_detector = HumanDetection()
face_detector = FaceLocationDetection()
landmarks_detector = FaceLandmarksDetection()

# Route for human location
@functions_router.route('/human_location', methods=['GET'])
def get_human_location():
    image_path = request.args.get('img_path')  # Get the image path from query parameter
    if image_path is None:
        return jsonify({'error': 'img_path parameter is missing'}), 400

    human_detector.image_path = image_path
    detected_boxes, detected_weights = human_detector.humanlocation()
    result = [{'box': box, 'weight': weight} for box, weight in zip(detected_boxes, detected_weights) if weight >= 0.5]
    return jsonify(result)

# Route for face landmarks
@functions_router.route('/face_landmarks', methods=['GET'])
def get_face_landmarks():
    image_path = request.args.get('img_path')  # Get the image path from query parameter
    if image_path is None:
        return jsonify({'error': 'img_path parameter is missing'}), 400

    landmarks_detector.image_path = image_path
    landmarks = landmarks_detector.facelandmarks()
    return jsonify(landmarks)

# Route for face location
@functions_router.route('/face_location', methods=['GET'])
def get_face_location():
    image_path = request.args.get('img_path')  # Get the image path from query parameter
    if image_path is None:
        return jsonify({'error': 'img_path parameter is missing'}), 400

    face_detector.image_path = image_path
    face_locations = face_detector.facelocation()
    return jsonify(face_locations)
