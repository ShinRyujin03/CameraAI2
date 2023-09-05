from flask import request
from app.routers.human_detection_routers import HumanDetection

def request_human_location_services():
    image_file = request.files['image']  # Access the uploaded file
    human_location = HumanDetection()
    human_result = human_location.get_human_location(image_file)
    return human_result
