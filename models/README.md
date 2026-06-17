# Models

This folder contains the machine learning models used by the Smart AI Cane project.

## Current Model

### YOLOv8 Nano (yolov8n.pt)

The current prototype uses the pretrained YOLOv8 Nano model provided by Ultralytics.

YOLO (You Only Look Once) is a real-time object detection model capable of identifying and locating objects within an image. The Nano version was selected because it provides fast inference speeds while maintaining reasonable detection accuracy, making it suitable for deployment on embedded and portable hardware.

### Objects Currently Used

The Smart AI Cane currently utilizes the following YOLOv8 object classes:

| Object     | YOLO Class ID |
| ---------- | ------------- |
| Person     | 0             |
| Chair      | 56            |
| Cell Phone | 67            |

When one of these objects is detected with sufficient confidence, the system generates an audio warning for the user.

### Audio Warnings

| Object     | Audio Output   |
| ---------- | -------------- |
| Person     | "Person ahead" |
| Chair      | "Chair"  |
| Cell Phone | "Phone ahead"  |

## Future Models

Future versions of the Smart AI Cane will incorporate custom-trained YOLO models for navigation-specific objects, including:

* Doors
* Stairs
* Shopping Carts
* Obstacles
* Walls

These custom models will improve the system's usefulness for visually impaired users by focusing on objects relevant to navigation and hazard avoidance.

## Model Source

Current model:

* yolov8n.pt (Ultralytics YOLOv8 Nano)

The model is loaded within the application using the Ultralytics Python package.
