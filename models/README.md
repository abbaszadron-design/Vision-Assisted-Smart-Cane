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

## Example Outputs
<img width="677" height="473" alt="image" src="https://github.com/user-attachments/assets/841ed823-54f4-48b3-a3f5-cc31454449a3" />
