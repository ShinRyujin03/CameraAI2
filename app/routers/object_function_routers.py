from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from schema import SchemaError
from app.sevices.human_detection import HumanDetection
from database.database import Database
import os
from app.handle.app_error import InvalidImageError, NoImageError

objects_router = Blueprint('object_router', __name__)
human_detector = HumanDetection()


@objects_router.route('/human_location', methods=['POST'])
def get_human_location():
    try:
        image_file = request.files['image']  # Access the uploaded file
        if not image_file:
            raise NoImageError

        # Check if the uploaded file has a valid image extension
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        filename, extension = os.path.splitext(image_file.filename)
        if extension[1:].lower() not in allowed_extensions:
            raise InvalidImageError

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

    except (SchemaError, InvalidImageError, NoImageError) as e:
        error_msg = str(e)
        return jsonify({'error': error_msg}), e.status_code
