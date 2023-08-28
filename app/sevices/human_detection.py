import cv2
import numpy as np
from ultralytics import YOLO
class HumanDetection:
    def __init__(self):
        self.image_data = None

    def humanlocation(self):
        # Load a pretrained YOLOv8n model
        model = YOLO('/Users/macbookairm1/Desktop/Viettel/cameraAI2/model/yolov8n.pt')
        # Convert image data to numpy array
        image_np = np.frombuffer(self.image_data, np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
        # Run inference on 'bus.jpg'
        results = model(image)  # results list
        detected_boxes = []
        detected_weights = []

        # Filter results based on the condition r.boxes.cls[i] == 0
        for r in results:
            cls_values = r.boxes.cls.tolist()  # Convert tensor to list
            for i, cls in enumerate(cls_values):
                if cls == 0:  # Only consider when cls is equal to 0
                    rounded_boxes = [round(value, 3) for value in r.boxes.xywh[i].tolist()]
                    detected_boxes.append(rounded_boxes)
                    detected_weights.append(
                        round(r.boxes.conf[i].item(), 3))  # Use .item() to convert scalar tensor to Python number

        return detected_boxes, detected_weights