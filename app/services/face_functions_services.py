from flask import request
from app.routers.face_functions_routers import FaceLocationDetection, FaceLandmarksDetection
def request_face_location_services(image_file):
    face_detector = FaceLocationDetection()
    face_result = face_detector.get_face_location(image_file)
    return face_result


def request_face_landmarks_services(image_file):
    face_landmarks = FaceLandmarksDetection()
    landmarks_result = face_landmarks.get_face_landmarks(image_file)
    return landmarks_result