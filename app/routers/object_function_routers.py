from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from schema import SchemaError
from app.sevices.human_detection import HumanDetection
from database.database import Database
objects_router = Blueprint('object_router', __name__)
human_detector = HumanDetection()

@objects_router.route('/human_location', methods=['POST'])
def get_human_location():
    try:
        image_file = request.files['image']  # Access the uploaded file
        if image_file:
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
            #return jsonify(result)
            return jsonify(result, {"message": f"Human location metadata of {image_name} saved successfully"})
        else:
            return jsonify({'error': 'No image file uploaded'}), 400
    except SchemaError as e:
        error_msg = str(e)
        return jsonify({'error': error_msg}), 400