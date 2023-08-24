import face_recognition
import cv2
import numpy as np
class FaceLocationDetection:
    def __init__(self):
        self.image_data = None

    def facelocation(self):
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        face_locations = face_recognition.face_locations(image)
        return face_locations
