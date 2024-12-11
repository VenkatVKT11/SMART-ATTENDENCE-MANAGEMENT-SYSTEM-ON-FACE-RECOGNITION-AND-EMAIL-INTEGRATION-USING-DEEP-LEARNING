import cv2
import face_recognition
import Numpy as np
import json
import os

# Initialize the face recognition database
known_faces = {}

def init_camera():
    return cv2.VideoCapture(0)

def load_known_faces():
    global known_faces
    try:
        with open('assets/known_faces.json', 'r') as file:
            known_faces = json.load(file)
            for name, data in known_faces.items():
                data['encoding'] = np.array(data['encoding'])
    except FileNotFoundError:
        known_faces = {}

def register_face(name, roll_no, cap):
    ret, image = cap.read()
    if not ret:
        print("Failed to capture image")
        return

    face_encoding = face_recognition.face_encodings(image)[0]
    known_faces[name] = {"roll_no": roll_no, "encoding": face_encoding}
    save_database()

def save_database():
    for name, data in known_faces.items():
        data['encoding'] = data['encoding'].tolist()
    with open('assets/known_faces.json', 'w') as file:
        json.dump(known_faces, file)

def capture_video(cap, video_label):
    # Implementation for capturing video frames and performing recognition
    pass
