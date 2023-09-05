from flask import Blueprint, request
from app.services.humen_detection_services import HumanDetection
objects_router = Blueprint('object_router', __name__)

@objects_router.route('/human_location', methods=['POST'])
def request_human_location():
    image_file = request.files['image']  # Access the uploaded file
    human_location = HumanDetection()
    human_result = human_location.get_human_location(image_file)
    return human_result

