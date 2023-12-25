import cv2
import numpy as np

class FaceLocationDrawer:
    def draw_face_locations(self, image_file, face_locations):
        face_locations = list(map(int, face_locations.split(",")))
        image_data = image_file.read()
        # Convert the image to RGB (OpenCV uses BGR by default)
        image_np = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Convert the flat list to a list of tuples
        face_locations = [(face_locations[i], face_locations[i + 1], face_locations[i + 2], face_locations[i + 3]) for i in range(0, len(face_locations), 4)]

        # Draw rectangles on the image for each face location
        for face_location in face_locations:
            top, right, bottom, left = face_location
            cv2.rectangle(image_rgb, (left, top), (right, bottom), (0, 0, 255), 2)
            # Convert the result image to bytes
        result_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
        _, buffer = cv2.imencode('.jpg', result_image)
        result_image_bytes = buffer.tobytes()
        return result_image_bytes
