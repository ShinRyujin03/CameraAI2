from flask import Blueprint, jsonify
from app.functions.human_detection import HumanDetection
from app.functions.face_location import FaceLocationDetection
from app.functions.face_landmarks import FaceLandmarksDetection
from database.database import Database
from config import Config
database_router = Blueprint('database_router', __name__)

@database_router.route('/save_face_location', methods=['POST'])
def save_face_location():
    face_detector = FaceLocationDetection()
    face_location = face_detector.facelocation()
    db = Database()

    db.insert_face_location(Config.img_name, face_location)
    db.close_connection()

    return jsonify({"message": "Face location data saved successfully"})
# ...

@database_router.route('/save_human_location', methods=['POST'])
def save_human_location():
    human_detector = HumanDetection()  # Assuming you have a HumanDetection class
    human_location_boxes, human_location_weights = human_detector.humanlocation()
    db = Database()

    db.insert_human_location(Config.img_name, human_location_boxes, human_location_weights)
    db.close_connection()

    return jsonify({"message": "Human location data saved successfully"})

@database_router.route('/save_face_landmark', methods=['POST'])
def save_face_landmark():
    face_landmark_detector = FaceLandmarksDetection()  # Assuming you have a FaceLandmarkDetection class
    face_landmarks = face_landmark_detector.facelandmarks()
    db = Database()
    db.insert_face_landmark(Config.img_name, face_landmarks)
    db.close_connection()

    return jsonify({"message": "Face landmark data saved successfully"})



