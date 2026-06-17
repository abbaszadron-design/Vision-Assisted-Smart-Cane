from ultralytics import YOLO
import cv2
import pygame
import time

# Load YOLO AI model
model = YOLO("yolov8n.pt")

# Initialize audio
pygame.mixer.init()

# Open webcam
cap = cv2.VideoCapture(0)

# Audio files
SOUNDS = {
    "Person ahead": "Sounds/person_ahead.wav",
    "Chair ahead": "Sounds/chair_ahead.wav",
    "Phone ahead": "Sounds/phone_ahead.wav",
    "Door ahead": "Sounds/door_ahead.wav",
    "Obstacle ahead": "Sounds/obstacle_ahead.wav"
}

# YOLO classes I care about for now
DETECTED_OBJECTS = {
    0: "Person ahead",   # person
    56: "Chair ahead",   # chair
    67: "Phone ahead"    # phone
}

# Last time each object was announced
last_spoken = {
    0: 0,
    56: 0,
    67: 0
}

cooldown = 5


def speak(message):

    print("SPEAK:", message)

    if message in SOUNDS:
        pygame.mixer.Sound(SOUNDS[message]).play()


while True:

    success, frame = cap.read()

    if not success:
        break

    results = model(frame)

    current_time = time.time()

    for box in results[0].boxes:

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        if class_id in DETECTED_OBJECTS and confidence > 0.80:

            if current_time - last_spoken[class_id] >= cooldown:

                message = DETECTED_OBJECTS[class_id]

                print(f"{message} | Confidence: {confidence:.2f}")

                speak(message)

                last_spoken[class_id] = current_time

    annotated_frame = results[0].plot()

    cv2.imshow("Smart Cane Vision", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
