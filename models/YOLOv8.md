# YOLOv8 Nano (yolov8n.pt)

This folder contains documentation and example outputs for the YOLOv8 Nano model used by the Smart AI Cane project.

## Model Overview

YOLOv8 Nano (yolov8n.pt) is a lightweight real-time object detection model developed by Ultralytics. The model is optimized for fast inference while maintaining good detection accuracy, making it suitable for portable and embedded AI applications.

## Current Usage

The Smart AI Cane currently uses YOLOv8 Nano to detect:

* Person (Class 0)
* Chair (Class 56)
* Cell Phone (Class 67)

Detected objects are highlighted with bounding boxes and confidence scores. When a supported object is detected with sufficient confidence, the system provides an audio warning to the user.

## How YOLOv8 Nano Works

YOLOv8 Nano (You Only Look Once) is a real-time object detection model that processes an image and identifies objects within a single pass of the neural network. The model outputs both the object classification and the location of the object using a bounding box around the object. 

For example, in the image below, the model detected a person with a confidence score of 92%. The bounding box indicates the location of the detected object, while the confidence score represents the model's certainty that the object belongs to a particular class. To reduce false detections, the Smart AI Cane uses a confidence threshold of 80%. Objects detected with a confidence score greater than or equal to 80% are considered valid detections and trigger the corresponding audio warning.

The Smart AI Cane currently uses YOLOv8 Nano to detect people, chairs, and cell phones from a live webcam feed. Each frame captured by the camera is processed by the model, and detections above a specified confidence threshold trigger an audio warning. For example, when a person is detected with high confidence, the system announces "Person ahead" through the audio output system.
<img width="677" height="473" alt="image" src="https://github.com/user-attachments/assets/841ed823-54f4-48b3-a3f5-cc31454449a3" />
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/ecb993dd-fc2f-449f-b26b-356f06c6e6d9" />
