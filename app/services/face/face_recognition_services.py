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

            unknown_encoding = face_recognition.face_encodings(unknown_face_image, unknown_face_locations, model="large")

            if not unknown_encoding:
                logging.error(NoDetection())
                raise NoDetection

            min_distance = float('inf')
            face_loaded = 0
            high_accuracy_name = []
            medium_accuracy_name = []
            low_accuracy_name = []
            for known_face in known_face_encodings:
                face_loaded = face_loaded + 1
                known_face_image = cv2.imdecode(np.frombuffer(known_face, np.uint8), cv2.IMREAD_COLOR)
                if known_face_image is not None:
                    known_encoding = face_recognition.face_encodings(known_face_image, None, model="large")
                    if known_encoding:
                        distance = face_recognition.face_distance(known_encoding, unknown_encoding[0])
                        last_min_distance = min_distance
                        min_distance = min(min_distance, distance[0])
                        recognized_face_name = known_face_names[face_loaded - 1]
                        if min_distance <= config.getfloat('face_function_config', 'high_accuracy_compare_face'):
                            if high_accuracy_name and min_distance < last_min_distance:
                                high_accuracy_name[0] = str(recognized_face_name)
                            else:
                                high_accuracy_name.append(str(recognized_face_name))
                        elif config.getfloat('face_function_config', 'high_accuracy_compare_face') < min_distance <= config.getfloat('face_function_config', 'medium_accuracy_compare_face'):
                            if medium_accuracy_name and min_distance < last_min_distance:
                                medium_accuracy_name[0] = str(recognized_face_name)
                            else:
                                medium_accuracy_name.append(str(recognized_face_name))
                        elif config.getfloat('face_function_config', 'medium_accuracy_compare_face') < min_distance <= config.getfloat('face_function_config', 'low_accuracy_compare_face'):
                            if low_accuracy_name and min_distance < last_min_distance:
                                low_accuracy_name[0] = str(recognized_face_name)
                            else:
                                low_accuracy_name.append(str(recognized_face_name))

            # Determine accuracy level after all distances have been calculated
            if min_distance <= config.getfloat('face_function_config', 'high_accuracy_compare_face'):
                accuracy = "High"
                print("Accuracy: High")
                print("Min distance:", min_distance)
                return high_accuracy_name[0], accuracy
            elif config.getfloat('face_function_config', 'high_accuracy_compare_face') < min_distance <= config.getfloat('face_function_config', 'medium_accuracy_compare_face'):
                accuracy = "Medium"
                print("Accuracy: Medium")
                print("Min distance:", min_distance)
                return medium_accuracy_name[0], accuracy
            elif config.getfloat('face_function_config', 'medium_accuracy_compare_face') < min_distance <= config.getfloat('face_function_config', 'low_accuracy_compare_face'):
                accuracy = "Low"
                print("Accuracy: Low")
                print("Min distance:", min_distance)
                return low_accuracy_name[0], accuracy
            else:
                accuracy = "Low"
                print("Accuracy: Low")
                print("Min distance:", min_distance)
                return "Unknown", accuracy
        except Exception as e:
            raise Exception
        finally:
            if high_accuracy_name:
                print("high_accuracy_name:", high_accuracy_name[0])
            else:
                print("high_accuracy_name: None")
            if medium_accuracy_name:
                print("medium_accuracy_name:", medium_accuracy_name[0])
            else:
                print("medium_accuracy_name: None")
            if low_accuracy_name:
                print("low_accuracy_name:", low_accuracy_name[0])
            else:
                print("low_accuracy_name: None")
            db.close_connection()

    def get_face_name_recognition(self,image_file):
        face_detector = NameRecognition()
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                image_name = secure_filename(image_file.filename)
                print("Image name:",image_name)
                logging.info(f'image_name: {image_name}')
                # Process the image using face_detector
                try:
                    recognized_face_name, accuracy = face_detector.face_name_recognition(image_data)
                except Exception:
                    raise Exception
                print(" ")
                # Create a response object
                result = {
                    'recognized_face_name': recognized_face_name,
                    'image_name': image_name,
                    'accuracy': accuracy
                }
                if len(recognized_face_name) == 0:
                    logging.error(NoDetection())
                    raise NoDetection
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                try:
                    logging.info(result)
                    return jsonify(result)
                except Exception as e:
                    return str(e)
