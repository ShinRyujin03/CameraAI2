import logging
from flask import Blueprint, request, jsonify
from app.handle.app_error import FileUnreachable
from app.services.objects.human_detection_services import HumanDetection

# Create instances of the function classes
objects_router = Blueprint('object_router', __name__)


# Route for human location
@objects_router.route('/human_location', methods=['POST'])
def request_human_location():
    try:
        image_files = request.files.getlist('image')  # Access the list of uploaded files
    except Exception:
        logging.error(FileUnreachable())
        raise FileUnreachable

    results = []

    human_location = HumanDetection()
    for image_file in image_files:
        human_result = human_location.get_human_location(image_file)
        results.append(human_result.get_json())  # Extract JSON content from each response

    return jsonify(results)

