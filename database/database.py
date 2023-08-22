import mysql.connector
from config import Config

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Config.db_host,
            user=Config.db_user,
            password=Config.db_password,
            database=Config.db_name
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

    def insert_face_landmark(self, image_name, landmarks):
        query = "INSERT INTO face_landmark (image_name, bottom_lip, chin, left_eye, left_eyebrow, nose_bridge, nose_tip, right_eye, right_eyebrow, top_lip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            image_name,
            str(landmarks['bottom_lip']),
            str(landmarks['chin']),
            str(landmarks['left_eye']),
            str(landmarks['left_eyebrow']),
            str(landmarks['nose_bridge']),
            str(landmarks['nose_tip']),
            str(landmarks['right_eye']),
            str(landmarks['right_eyebrow']),
            str(landmarks['top_lip'])
        )
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
