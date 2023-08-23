from flask import Blueprint, jsonify, request
from app.functions.human_detection import HumanDetection
from app.functions.face_location import FaceLocationDetection
from app.functions.face_landmarks import FaceLandmarksDetection
from database.database import Database
import os
database_router = Blueprint('database_router', __name__)

# Create instances of the function classes
human_detector = HumanDetection()
face_detector = FaceLocationDetection()
face_landmark_detector = FaceLandmarksDetection()

@database_router.route('/save_face_location', methods=['POST'])
def save_face_location():
    image_path = request.args.get('img_path')  # Get the image path from query parameter
    if image_path is None:
        return jsonify({'error': 'img_path parameter is missing'}), 400
    img_name = os.path.basename(image_path)

    # Load the image file using PIL
    with open(image_path, 'rb') as img_file:
        face_detector.image_path = img_file
        face_location = face_detector.facelocation()

    db = Database()
    db.insert_face_location(img_name, face_location)
    db.close_connection()
    return jsonify({"message": f"Face location metadata of {img_name} saved successfully"})
# ...

@database_router.route('/save_human_location', methods=['POST'])
def save_human_location():
    human_location_boxes, human_location_weights = human_detector.humanlocation()
    db = Database()
    image_path = request.args.get('img_path')  # Get the image path from query parameter
    if image_path is None:
        return jsonify({'error': 'img_path parameter is missing'}), 400
    img_name = os.path.basename(image_path)
    db.insert_human_location(img_name, human_location_boxes, human_location_weights)
    db.close_connection()

    return jsonify({"message": f"Human location metadata of {img_name} saved successfully"})

@database_router.route('/save_face_landmark', methods=['POST'])
def save_face_landmark():
    face_landmarks = face_landmark_detector.facelandmarks()
    db = Database()
    image_path = request.args.get('img_path')  # Get the image path from query parameter
    if image_path is None:
        return jsonify({'error': 'img_path parameter is missing'}), 400
    img_name = os.path.basename(image_path)
    db.insert_face_landmark(img_name, face_landmarks)
    db.close_connection()

    return jsonify({"message": f"Face landmark metadata of {img_name} saved successfully"})



