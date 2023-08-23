import cv2
from config import Config
class HumanDetection:
    def __init__(self):
        self.image_path = Config.img_path

    def humanlocation(self):
        # initialize the HOG descriptor/person detector
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        image = cv2.imread(self.image_path)
        image = cv2.resize(image, (640, 480))
        # using a greyscale picture, also for faster detection
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # detect people in the image
        # returns the bounding boxes for the detected objects
        boxes, weights = hog.detectMultiScale(image, winStride=(8, 8))
        return boxes, weights
