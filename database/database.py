import sqlite3

class MetadataDB:
    def __init__(self, db_name='face_metadata.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS human_locations (
                id INTEGER PRIMARY KEY,
                image_path TEXT,
                x INTEGER,
                y INTEGER,
                width INTEGER,
                height INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS face_landmarks (
                id INTEGER PRIMARY KEY,
                image_path TEXT,
                landmark_name TEXT,
                x INTEGER,
                y INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS face_locations (
                id INTEGER PRIMARY KEY,
                image_path TEXT,
                x INTEGER,
                y INTEGER,
                width INTEGER,
                height INTEGER
            )
        ''')

        self.conn.commit()

    def insert_human_location(self, image_path, x, y, width, height):
        query = '''
            INSERT INTO human_locations (image_path, x, y, width, height)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (image_path, x, y, width, height))
        self.conn.commit()

    def insert_face_landmark(self, image_path, landmark_name, x, y):
        query = '''
            INSERT INTO face_landmarks (image_path, landmark_name, x, y)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.execute(query, (image_path, landmark_name, x, y))
        self.conn.commit()

    def insert_face_location(self, image_path, x, y, width, height):
        query = '''
            INSERT INTO face_locations (image_path, x, y, width, height)
            VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (image_path, x, y, width, height))
        self.conn.commit()

    def insert_face_location_data(self, image_path, face_locations):
        for location in face_locations:
            x, y, w, h = location
            self.insert_face_location(image_path, x, y, w, h)

    def insert_human_location_data(self, image_path, boxes):
        for box in boxes:
            x, y, w, h = box
            self.insert_human_location(image_path, x, y, w, h)

    def insert_face_landmarks_data(self, image_path, face_landmarks_list):
        for landmarks in face_landmarks_list:
            for landmark_name, points in landmarks.items():
                for point in points:
                    x, y = point
                    self.insert_face_landmark(image_path, landmark_name, x, y)

    def close_connection(self):
        self.conn.close()
