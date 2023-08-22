from flask import Blueprint, request, jsonify
from app.funtion.human_detection import HumanDetection
from app.funtion.face_location import FaceLocationDetection
from app.funtion.face_landmarks import FaceLandmarksDetection
from database.database import Database

database_router = Blueprint('database_router', __name__)

@database_router.route('/save_face_location', methods=['POST'])
def save_face_location():
    data = request.get_json()
    image_name = data.get('image_name')
    face_location = data.get('face_location')

    face_detector = FaceLocationDetection()
    db = Database()

    face_detector.save_to_database(image_name, face_location)
    db.close_connection()

    return jsonify({"message": "Face location data saved successfully"})
# ...

@database_router.route('/save_human_location', methods=['POST'])
def save_human_location():
    data = request.get_json()
    image_name = data.get('image_name')
    human_location_boxes = data.get('human_location_boxes')
    human_location_weights = data.get('human_location_weights')

    human_detector = HumanDetection()  # Assuming you have a HumanDetection class
    db = Database()

    human_detector.save_to_database(image_name, human_location_boxes, human_location_weights)
    db.close_connection()

    return jsonify({"message": "Human location data saved successfully"})

@database_router.route('/save_face_landmark', methods=['POST'])
def save_face_landmark():
    data = request.get_json()
    image_name = data.get('image_name')
    face_landmarks = data.get('face_landmarks')

    face_landmark_detector = FaceLandmarksDetection()  # Assuming you have a FaceLandmarkDetection class
    db = Database()

    face_landmark_detector.save_to_database(image_name, face_landmarks)
    db.close_connection()

    return jsonify({"message": "Face landmark data saved successfully"})

# ...


