import face_recognition
from config import Config
class FaceLocationDetection:
    def __init__(self):
        self.image_path = Config.img_path

    def facelocation(self):
        image = face_recognition.load_image_file(self.image_path)
        face_locations = face_recognition.face_locations(image)
        return face_locations

