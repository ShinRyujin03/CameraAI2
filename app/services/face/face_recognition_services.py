import mysql
from flask import jsonify
from werkzeug.utils import secure_filename
from app.schema.image_schema import *
from database.database import Database
import face_recognition
import cv2
import numpy as np
from app.handle.app_error import DatabaseNoneError, NoDetection
from app.services.face.face_detection_services import FaceLocationDetection
import logging
import mysql.connector
import configparser

# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")
# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)

class NameRecognition:
    def __init__(self):
        self.image_data = None

    def face_name_recognition(self, unknown_face):
        db = Database()
        try:
            known_face_encodings, known_face_names = db.get_image_files_and_name()
            # Convert the uploaded face to an encoding
            unknown_face_image = cv2.imdecode(np.frombuffer(unknown_face, np.uint8), cv2.IMREAD_COLOR)

            # Get face locations using face_detector
            unknown_face_detector = FaceLocationDetection()
            unknown_face_detector.image_data = unknown_face
            unknown_face_locations = unknown_face_detector.facelocation()

            unknown_encoding = face_recognition.face_encodings(unknown_face_image, unknown_face_locations,
                                                               model="large")

            if not unknown_encoding:
                logging.error(NoDetection())
                raise NoDetection

            min_distance = float('inf')
            recognized_face_name = "Unknown"
            face_loaded = 0
            for known_face in known_face_encodings:
                face_loaded = face_loaded + 1
                known_face_image = cv2.imdecode(np.frombuffer(known_face, np.uint8), cv2.IMREAD_COLOR)
                if known_face_image is not None:
                    known_encoding = face_recognition.face_encodings(known_face_image, None, model="large")
                    if known_encoding:
                        distance = face_recognition.face_distance(known_encoding, unknown_encoding[0])
                        min_distance = min(min_distance, distance[0])
                        recognized_face_name = known_face_names[face_loaded-1]
                        if min_distance <= 0.33:
                            print("Min distance:", min_distance)
                            return recognized_face_name
            if min_distance > 0.33:
                print("Min distance:", min_distance)
                return "Unknown"
        except Exception as e:
            raise Exception
        finally:
            db.close_connection()

    def get_face_name_recognition(self,image_file):
        face_detector = NameRecognition()
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                image_name = secure_filename(image_file.filename)
                logging.info(f'image_name: {image_name}')
                # Process the image using face_detector
                recognized_face_name = face_detector.face_name_recognition(image_data)
                print(" ")
                # Create a response object
                result = {
                    'recognized_face_name': recognized_face_name,
                    'image_name': image_name
                }
                if len(recognized_face_name) == 0:
                    logging.error(NoDetection())
                    raise NoDetection
                #db = Database()
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                try:
                    #db.insert_face_verify_status(image_name, face_name, verify)
                    #db.close_connection()
                    logging.info(result)
                    return jsonify(result)
                except Exception as e:
                    return str(e)
