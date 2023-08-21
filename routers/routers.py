from flask import Flask, jsonify
from app.funtion.human_detection import HumanDetection
from app.funtion.face_location import FaceLocationDetection
from app.funtion.face_landmarks import FaceLandmarksDetection
app = Flask(__name__)

# Create instances of the function classes
human_detector = HumanDetection()
face_detector = FaceLocationDetection()
landmarks_detector = FaceLandmarksDetection()

# Route for human location
@app.route('/human_location', methods=['GET'])
def get_human_location():
    detected_boxes, detected_weights = human_detector.humanlocation()
    result = [{'box': box.tolist(), 'weight': weight} for box, weight in zip(detected_boxes, detected_weights)]
    return jsonify(result)

# Route for face landmarks
@app.route('/face_landmarks', methods=['GET'])
def get_face_landmarks():
    landmarks = landmarks_detector.facelandmarks()
    return jsonify(landmarks)

# Route for face location
@app.route('/face_location', methods=['GET'])
def get_face_location():
    face_locations = face_detector.facelocation()
    return jsonify(face_locations)

if __name__ == '__main__':
    app.run(debug=True)
