import mysql
from flask import jsonify
from werkzeug.utils import secure_filename
from app.schema.image_schema import *
from database.database import Database
import face_recognition
import cv2
import numpy as np
from app.handle.app_error import DatabaseNoneError, NoDetection, NoFaceNameError
from app.services.face.face_detection_services import FaceLocationDetection
import logging
import mysql.connector
import configparser

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

            unknown_encoding = face_recognition.face_encodings(unknown_face_image, unknown_face_locations,model="large")

            if not unknown_encoding:
                logging.error(NoDetection())
                raise NoDetection

            min_distance = float('inf')
            face_loaded = 0
            for known_face in known_face_encodings:
                face_loaded = face_loaded + 1
                known_face_image = cv2.imdecode(np.frombuffer(known_face, np.uint8), cv2.IMREAD_COLOR)
                if known_face_image is not None:
                    known_encoding = face_recognition.face_encodings(known_face_image, None, model="large")
                    if known_encoding:
                        distance = face_recognition.face_distance(known_encoding, unknown_encoding[0])
                        min_distance = min(min_distance, distance[0])
                        if min_distance <= config.getfloat('function_config', 'high_accuracy_compare_face'):
                            break
            if min_distance <= config.getfloat('function_config', 'high_accuracy_compare_face'):
                print("Accuracy: High")
                print("Min distance:", min_distance)
                print("Number of loaded face:", face_loaded)
                return "verified"
            if config.getfloat('function_config', 'high_accuracy_compare_face') < min_distance <= config.getfloat('function_config', 'medium_accuracy_compare_face'):
                print("Accuracy: Medium")
                print("Min distance:", min_distance)
                print("Number of loaded face:", face_loaded)
                return "verified"
            elif config.getfloat('function_config', 'medium_accuracy_compare_face') < min_distance <= config.getfloat('function_config', 'low_accuracy_compare_face'):
                print("Accuracy: Low")
                print("Min distance:", min_distance)
                print("Number of loaded face:", face_loaded)
                return "verified"
            else:
                print("Min distance:", min_distance)
                return "not verified"
        except Exception as e:
            return str(e)
        finally:
            db.close_connection()

    def get_face_verification(self,image_file, face_name):
        face_detector = FaceVerification()
        if not face_name:
            logging.error(NoFaceNameError())
            raise NoFaceNameError
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                image_name = secure_filename(image_file.filename)
                print("Image name:",image_name)
                logging.info(f'image_name: {image_name}')
                # Process the image using face_detector
                verify = face_detector.face_verification(image_data)
                print(" ")
                # Create a response object
                result = {
                    'face_verification': verify,
                    'Name': face_name,
                    'image_name': image_name
                }
                if len(face_name) == 0:
                    logging.error(NoDetection())
                    raise NoDetection
                db = Database()
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                try:
                    db.insert_face_verify_status(image_name, face_name, verify)
                    db.close_connection()
                    logging.info(result)
                    return jsonify(result)
                except Exception as e:
                    return str(e)
