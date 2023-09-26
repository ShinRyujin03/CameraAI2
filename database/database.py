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

    def insert_image_file(self, image_name, image_file):
        query = "INSERT INTO image (image_name, image_file) VALUES (%s, %s)"
        values = (image_name, str(image_file))
        self.cursor.execute(query, values)
        self.conn.commit()

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
    def insert_face_emotions(self, image_name, face_locations, emotions, emotion_weights):
        query = "INSERT INTO face_emotions (image_name, face_locations, emotions, emotion_weights) VALUES (%s, %s, %s, %s)"
        values = (image_name, str(face_locations), str(emotions), str(emotion_weights))
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_all_image_files(self):
        query = "SELECT image_file FROM image"

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        image_files = [result[0] for result in results]

        return image_files
    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()