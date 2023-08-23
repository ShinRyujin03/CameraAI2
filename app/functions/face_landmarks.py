import face_recognition
import os
class FaceLandmarksDetection:
    def __init__(self):
        self.image_path = ''
        self.img_name = os.path.basename(self.image_path)

    def facelandmarks(self):
        image = face_recognition.load_image_file(self.image_path)
        face_landmarks_list = face_recognition.face_landmarks(image)
        return face_landmarks_list
