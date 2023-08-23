import cv2
import os
class HumanDetection:
    def __init__(self):
        self.image_path = ''
        self.img_name = os.path.basename(self.image_path)
    def humanlocation(self):
        # initialize the HOG descriptor/person detector
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        image = cv2.imread(self.image_path)
        # using a greyscale picture, also for faster detection
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(image, winStride=(8, 8))

        # Filter the results based on weights >= 0.5
        filtered_boxes = []
        filtered_weights = []
        for box, weight in zip(boxes, weights):
            if weight >= 0.5:
                filtered_boxes.append(box.tolist())
                filtered_weights.append(weight)

        return filtered_boxes, filtered_weights

