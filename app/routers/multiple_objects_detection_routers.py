import logging
from flask import Blueprint, request, jsonify
from app.handle.app_error import FileUnreachable
from app.services.objects.multiple_objects_detection_services import MultipleObjectDetection

# Create instances of the function classes
multiple_objects_router = Blueprint('multiple_object_router', __name__)


# Route for human location
@multiple_objects_router.route('/m_object_location', methods=['POST'])
def request_objects_location():
    try:
        image_files = request.files.getlist('image')  # Access the list of uploaded files
    except Exception:
        logging.error(FileUnreachable())
        raise FileUnreachable

    results = []

    objects_location = MultipleObjectDetection()
    for image_file in image_files:
        objects_result = objects_location.get_objects_location(image_file)
        results.append(objects_result.get_json())  # Extract JSON content from each response

    return jsonify(results)

