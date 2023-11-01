import cv2
import numpy as np


class FaceLocationDrawer:
    def draw_face_locations(self, image, face_locations):
        # Convert the image to RGB (OpenCV uses BGR by default)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Draw rectangles on the image for each face location
        for face_location in face_locations:
            top, right, bottom, left = face_location
            cv2.rectangle(image_rgb, (left, top), (right, bottom), (0, 0, 255), 2)

        return cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)


# Usage example
image = cv2.imread("/Users/macbookairm1/Desktop/K-Pop/IVE/Snapinsta.app_387269765_6448350551957565_5189336302001287490_n_1080.jpg")
face_locations = [(769, 1612, 924, 1457), (288, 459, 442, 304), (383, 1515, 512, 1386), (125, 841, 254, 712), (219, 1990, 374, 1835), (139, 1199, 268, 1070)]  # Example face locations

drawer = FaceLocationDrawer()
result_image = drawer.draw_face_locations(image, face_locations)

# Display the result
cv2.imshow("Face Locations", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
