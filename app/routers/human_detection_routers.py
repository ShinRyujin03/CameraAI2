from flask import Blueprint, request
from app.services.human_detection_services import HumanDetection
# Create instances of the function classes
objects_router = Blueprint('object_router', __name__)

# Route for human location
@objects_router.route('/human_location', methods=['POST'])
def request_human_location():
    image_file = request.files['image']  # Access the uploaded file
    human_location = HumanDetection()
    human_result = human_location.get_human_location(image_file)
    return human_result

