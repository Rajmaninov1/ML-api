import cv2
import numpy as np
from ultralytics import YOLO

from schemas.yolo.yolo_img_predictions import Detection, ImgCoords

model = YOLO("yolov8n.pt")


async def yolo_predict_img(image_bytes: bytes) -> list:
    # Process the uploaded image for object detection
    image = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # Perform object detection with YOLOv8
    detections = model.predict(image)[0]

    detections_list = []
    for i, detection in enumerate(detections.boxes.cls):
        name = next(iter([name for key, name in detections.names.items() if key == detection]), None)
        img_coords = [tensor.item() for tensor in detections.boxes.xyxy[i]]
        detections_list.append(Detection(
            detection_type=name,
            confidence=detections.boxes.conf[i].item(),
            bbox=ImgCoords(
                x_min=img_coords[0],
                y_min=img_coords[1],
                x_max=img_coords[2],
                y_max=img_coords[3]
            )
        ))

    return detections_list
