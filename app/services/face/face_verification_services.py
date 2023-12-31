import re
import time

import cv2
import face_recognition
import mysql
import mysql.connector
import numpy as np
from flask import jsonify
from werkzeug.utils import secure_filename

from app.handle.app_error import DatabaseNoneError, NoDetection, InvalidFaceNameError, NoFaceNameError
from app.schema.image_schema import *
from app.services.face.face_detection_services import FaceLocationDetection
from database.database import Database

# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")
# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)


class FaceVerification:
    def __init__(self):
        self.image_data = None

    def face_verification(self, unknown_face):
        db = Database()
        try:
            known_face_encodings = db.get_all_image_files()
            print("Known face nums:", len(known_face_encodings))
            # Convert the uploaded face to an encoding
            unknown_face_image = cv2.imdecode(np.frombuffer(unknown_face, np.uint8), cv2.IMREAD_COLOR)

            # Get face locations using face_detector
            unknown_face_detector = FaceLocationDetection()
            unknown_face_detector.image_data = unknown_face
            unknown_face_locations = unknown_face_detector.facelocation()
            if len(unknown_face_locations) == 0:
                logging.error(NoDetection())
                raise NoDetection
            unknown_encoding = face_recognition.face_encodings(unknown_face_image, unknown_face_locations,
                                                               model="large")

            min_distance = float('inf')
            face_loaded = 0
            start_time = time.time()
            high_accuracy_threshold = config.getfloat('verification_config', 'high_accuracy_verification')
            medium_accuracy_threshold = config.getfloat('verification_config', 'medium_accuracy_verification')
            low_accuracy_threshold = config.getfloat('verification_config', 'low_accuracy_verification')

            for known_face in known_face_encodings:
                face_loaded = face_loaded + 1
                known_face_image = cv2.imdecode(np.frombuffer(known_face, np.uint8), cv2.IMREAD_COLOR)
                if known_face_image is not None:
                    known_encoding = face_recognition.face_encodings(known_face_image, None, model="large")
                    if known_encoding:
                        distance = face_recognition.face_distance(known_encoding, unknown_encoding[0])
                        min_distance = min(min_distance, distance[0])
                        elapsed_time = time.time() - start_time
                        if min_distance <= high_accuracy_threshold or elapsed_time >= config.getint('verification_config','verification_elapsed_time'):
                            break
            if min_distance <= high_accuracy_threshold + config.getfloat('verification_config', 'delta_distance'):
                if min_distance <= high_accuracy_threshold:
                    accuracy = "High"
                    print("Accuracy: High")
                else:
                    accuracy = "Medium-high"
                    print("Accuracy: Medium-high")
                print("Min distance:", min_distance)
                print("Number of loaded face:", face_loaded)
                verify = "verified"
                return accuracy, verify
            if high_accuracy_threshold + config.getfloat('verification_config', 'delta_distance') < min_distance <= medium_accuracy_threshold:
                accuracy = "Medium-low"
                print("Accuracy: Medium-low")
                print("Min distance:", min_distance)
                print("Number of loaded face:", face_loaded)
                verify = "not verified"
                return accuracy, verify
            elif medium_accuracy_threshold < min_distance <= low_accuracy_threshold:
                accuracy = "Low"
                print("Accuracy: Low")
                print("Min distance:", min_distance)
                print("Number of loaded face:", face_loaded)
                verify = "not verified"
                return accuracy, verify
            else:
                accuracy = "Low"
                print("Min distance:", min_distance)
                verify = "not verified"
                return accuracy, verify
        finally:
            db.close_connection()

    def get_face_verification(self, image_file, face_name):
        face_detector = FaceVerification()
        if not face_name:
            logging.error(NoFaceNameError())
            raise NoFaceNameError()
        else:
            if not re.match("^[a-zA-Z]+$", face_name):
                logging.error(InvalidFaceNameError())
                raise InvalidFaceNameError()
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                image_name = secure_filename(image_file.filename)
                print("Image name:", image_name)
                logging.info(f'image_name: {image_name}')
                # Process the image using face_detector
                accuracy, verify = face_detector.face_verification(image_data)
                print(" ")
                # Create a response object
                result = {
                    'face_verification': verify,
                    'Accuracy': accuracy,
                    'Name': face_name,
                    'image_name': image_name
                }
                db = Database()
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                try:
                    logging.info(result)
                    db.insert_face_verify_status(image_name, face_name, verify)
                    if accuracy == "High":
                        db.insert_image_file(image_name, image_data)
                        return jsonify(result, {"message": f"Image {image_name} saved successfully"})
                    db.close_connection()
                    return jsonify(result)
                except Exception as e:
                    return str(e)
