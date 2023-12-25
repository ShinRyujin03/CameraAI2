import cv2
import numpy as np

class FaceLocationDrawer:
    def draw_face_locations(self, image_file, face_locations, zoom_factor):
        if not zoom_factor:
            zoom_factor = 1.0
        else:
            zoom_factor = float(zoom_factor)
            if zoom_factor == 0:
                zoom_factor = 1.0
        face_locations = list(map(int, face_locations.split(",")))
        image_data = image_file.read()
        # Convert the image to RGB (OpenCV uses BGR by default)
        image_np = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Apply zoom factor
        image_rgb_zoomed = cv2.resize(image_rgb, None, fx=zoom_factor, fy=zoom_factor)

        # Convert the flat list to a list of tuples
        face_locations = [
            (int(location[0] * zoom_factor), int(location[1] * zoom_factor),
             int(location[2] * zoom_factor), int(location[3] * zoom_factor))
            for location in zip(*[iter(face_locations)] * 4)
        ]

        # Draw rectangles on the zoomed image for each face location
        for face_location in face_locations:
            top, right, bottom, left = face_location
            cv2.rectangle(image_rgb_zoomed, (left, top), (right, bottom), (0, 0, 255), 2)

        # Convert the result image to bytes
        result_image = cv2.cvtColor(image_rgb_zoomed, cv2.COLOR_RGB2BGR)
        _, buffer = cv2.imencode('.jpg', result_image)
        result_image_bytes = buffer.tobytes()
        return result_image_bytes
