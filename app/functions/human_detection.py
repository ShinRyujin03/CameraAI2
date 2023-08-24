import cv2
import numpy as np

class HumanDetection:
    def __init__(self):
        self.image_data = None

    def humanlocation(self):
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        # Convert image data to numpy array
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        boxes, weights = hog.detectMultiScale(gray, winStride=(8, 8), padding=(16, 16))

        # Filter the results based on weights >= 0.5
        filtered_boxes = []
        filtered_weights = []
        for box, weight in zip(boxes, weights):
            if weight >= 0.5:
                filtered_boxes.append(box.tolist())
                filtered_weights.append(weight)

        return filtered_boxes, filtered_weights
