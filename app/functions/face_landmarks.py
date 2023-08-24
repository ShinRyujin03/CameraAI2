import face_recognition
import cv2
import numpy as np
class FaceLandmarksDetection:
    def __init__(self):
        self.image_data = None

    def facelandmarks(self):
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        face_landmarks_list = face_recognition.face_landmarks(image)
        return face_landmarks_list
