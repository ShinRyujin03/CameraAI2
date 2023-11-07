import configparser
import os

import mysql.connector

# Construct the relative path to config.ini
config_path = os.path.realpath("../config.ini")
# Create a configuration object
config = configparser.ConfigParser()
config.read(config_path)


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=config.get('db_config', 'db_host'),
            user=config.get('db_config', 'db_user'),
            password=config.get('db_config', 'db_password'),
            database=config.get('db_config', 'db_name')
        )
        self.cursor = self.conn.cursor()

    def insert_image_file(self, image_name, image_file):
        # Check if the image_name already exists in the table
        check_query = "SELECT COUNT(*) FROM image WHERE image_name = %s"
        self.cursor.execute(check_query, (image_name,))
        count = self.cursor.fetchone()[0]

        if count == 0:
            # Insert the new image if image_name doesn't exist
            insert_query = "INSERT INTO image (image_name, image_file) VALUES (%s, %s)"
            values = (image_name, image_file)
            self.cursor.execute(insert_query, values)
            self.conn.commit()
        else:
            pass

    def insert_face_location(self, image_name, face_location):
        query = "INSERT INTO face_location (image_name, face_location) VALUES (%s, %s)"
        values = (image_name, str(face_location))
        self.cursor.execute(query, values)
        self.conn.commit()

    def insert_human_location(self, image_name, boxes, weights):
        query = "INSERT INTO human_location (image_name, human_location_boxes, human_location_weights) VALUES (%s, %s, %s)"
        values = (image_name, str(boxes), str(weights))
        self.cursor.execute(query, values)
        self.conn.commit()

    def insert_detected_objects(self, image_name, objects_name, boxes, weights):
        query = "INSERT INTO detected_objects (image_name, objects_name, objects_location_boxes ,objects_location_weights) VALUES (%s, %s, %s, %s)"
        values = (image_name, str(objects_name), str(boxes), str(weights))
        self.cursor.execute(query, values)
        self.conn.commit()

    def insert_face_landmark(self, image_name, landmarks_data):
        for landmarks in landmarks_data:
            bottom_lip = str(landmarks.get('bottom_lip'))
            chin = str(landmarks.get('chin'))
            left_eye = str(landmarks.get('left_eye'))
            left_eyebrow = str(landmarks.get('left_eyebrow'))
            nose_bridge = str(landmarks.get('nose_bridge'))
            nose_tip = str(landmarks.get('nose_tip'))
            right_eye = str(landmarks.get('right_eye'))
            right_eyebrow = str(landmarks.get('right_eyebrow'))
            top_lip = str(landmarks.get('top_lip'))

            query = "INSERT INTO face_landmark (image_name, bottom_lip, chin, left_eye, left_eyebrow, nose_bridge, nose_tip, right_eye, right_eyebrow, top_lip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                image_name,
                bottom_lip,
                chin,
                left_eye,
                left_eyebrow,
                nose_bridge,
                nose_tip,
                right_eye,
                right_eyebrow,
                top_lip
            )

            self.cursor.execute(query, values)
        self.conn.commit()

    def insert_face_facial_attubute(self, image_name, emotions, ages, gender):
        query = "INSERT INTO face_facial_attribute (image_name, emotions, ages, gender) VALUES (%s, %s, %s, %s)"
        values = (image_name, str(emotions), str(ages), str(gender))
        self.cursor.execute(query, values)
        self.conn.commit()

    def insert_face_verify_status(self, image_name, face_name, verify_status):
        query = "INSERT INTO face_verified (image_name, face_name, verify_status) VALUES (%s, %s, %s)"
        values = (image_name, face_name, verify_status)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_all_image_files(self):
        query = "SELECT image_file FROM image"

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        image_files = [result[0] for result in results]
        # image_bytes_list = [base64.b64decode(base64_string) for base64_string in image_files]
        return image_files

    def get_image_files_and_name(self):
        query = "SELECT image_file, face_name FROM face_metadata WHERE face_name IS NOT NULL AND image_file IS NOT NULL"

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        image_files = [result[0] for result in results if result[0] is not None]
        face_names = [result[1] for result in results if result[1] is not None]

        return image_files, face_names

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
