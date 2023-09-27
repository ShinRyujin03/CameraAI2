import mysql
from flask import jsonify
from werkzeug.utils import secure_filename
from app.schema.image_schema import *
from database.database import Database
import face_recognition
import cv2
import numpy as np
from app.handle.app_error import DatabaseNoneError, NoDetection, OutputTooLongError
import logging
import base64

class FaceLocationDetection:
    def __init__(self):
        self.image_data = None

    def facelocation(self):
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        face_locations = face_recognition.face_locations(image)
        return face_locations
    def get_face_location(self,image_file):
        face_detector = FaceLocationDetection()
        if schema_test(image_file) == True:
            try:
                # Read the image data from the file
                image_data = image_file.read()
                # Convert the bytes to base64
                base64_image = base64.b64encode(image_data)
                base64_image_string = base64_image.decode('utf-8')
                image_name = secure_filename(image_file.filename)
                logging.info(f'image_name: {image_name}')
                # Process the image using face_detector
                face_detector.image_data = image_data
                face_locations = face_detector.facelocation()
                # Create a response object
                result = {
                    'face_locations': face_locations,
                    'image_name': image_name
                }
                if len(face_locations) == 0:
                    logging.error(NoDetection())
                    raise NoDetection
                db = Database()
            except mysql.connector.Error:
                logging.error(DatabaseNoneError())
                raise DatabaseNoneError
            else:
                if len(str(face_locations)) > 500:
                    logging.error(OutputTooLongError())
                    raise OutputTooLongError
                else:
                    db.insert_face_location(image_name, face_locations)
                    db.insert_image_file(image_name, image_data)
                    db.close_connection()
                    logging.info(result, {"message": f"Face location metadata of {image_name} saved successfully"})
                    return jsonify(result, {"message": f"Face location metadata of {image_name} saved successfully"})

