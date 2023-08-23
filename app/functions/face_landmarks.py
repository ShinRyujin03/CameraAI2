import face_recognition
from config import Config
class FaceLandmarksDetection:
    def __init__(self):
        self.image_path = Config.img_path

    def facelandmarks(self):
        image = face_recognition.load_image_file(self.image_path)
        face_landmarks_list = face_recognition.face_landmarks(image)
        return face_landmarks_list
