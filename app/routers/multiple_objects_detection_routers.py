from flask import Blueprint, request
from app.handle.app_error import FileUnreachable
from app.services.objects.multiple_objects_detection_services import MultipleObjectDetection

# Create instances of the function classes
multiple_objects_router = Blueprint('multiple_object_router', __name__)


# Route for human location
@multiple_objects_router.route('/m_object_location', methods=['POST'])
def request_objects_location():
    try:
        image_file = request.files['image']  # Access the uploaded file
    except Exception:
        raise FileUnreachable
    objects_location = MultipleObjectDetection()
    objects_result = objects_location.get_objects_location(image_file)
    return objects_result
