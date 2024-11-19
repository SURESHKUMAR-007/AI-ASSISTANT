import cv2
import numpy as np
from PIL import Image
import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_objects(image):
    """Detect objects in an image and return annotated image and labels."""
    image_np = np.array(image)
    results = model(image_np)

    # Annotate image with bounding boxes
    annotated_image = np.squeeze(results.render())
    labels = results.pandas().xyxy[0]['name'].tolist()
    return Image.fromarray(annotated_image), labels