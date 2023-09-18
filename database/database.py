import mysql.connector
import configparser
import os

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

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()