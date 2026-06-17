# Smart AI Cane

This project is designed to help visually impaired users navigate their surroundings more safely and independently.

The goal of this project is to combine computer vision, distance sensors, and audio feedback into a portable device that can be attached to a cane. The system will detect people, doors, chairs, stairs, and other common obstacles, then provide real-time audio warnings to the user.

## Hardware

* Arduino UNO Q 4GB
* Logitech C270 Webcam
* VL53L1X ToF Distance Sensors (13ft max)
* Bluetooth Earbuds
* 10000mAh 45W USB-C PD Power Bank
* 7-in-1 USB-C Hub

## Software

* Python
* OpenCV
* Ultralytics YOLO
* Text-to-Speech libraries
* Custom-trained object detection models

## Project Goals

The primary goal is to create a working prototype capable of assisting visually impaired users by detecting important objects and hazards in real time.


<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/c942a481-0b81-4d45-aff4-99a0be7c0376" />


### Navigation and Hazard Detection System

A forward-facing camera will continuously capture images of the environment, which are processed by custom AI object detection models to identify important navigation features such as obstacles, walls, stairs, doors, and other hazards.

To improve reliability, the system also utilizes Time-of-Flight (ToF) distance sensors mounted on the cane. While the AI model determines what object is present, the ToF sensors measure how far away the detected object is from the user. By combining object classification with real-time distance measurements, the system can determine both the type of hazard and its proximity.

Once an object is identified and its distance is calculated, the Smart AI Cane generates an audio alert through the integrated text-to-speech system. For example, the system may announce messages such as "Obstacle ahead, 2 meters," "Stairs ahead," or "Wall ahead, 1 meter." This allows the user to receive immediate feedback about changes in the environment and make safer navigation decisions while walking.

The long-term goal of this project is to create a portable and affordable assistive device capable of providing real-time environmental awareness and improving mobility for visually impaired individuals.

## System Diagram
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/41ead798-5adb-44f8-94ea-642670812c09" />


## Prototype Layout 
<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/f13dc7d0-8e10-4838-a6a6-b358b68af960" />
