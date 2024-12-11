import tkinter as tk
from tkinter import messagebox
from face_recognition import register_face, capture_video, save_database
from email_handler import send_email_with_attachment
from utils import display_attendance_list

def setup_gui(root, cap):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Header Label
    label = tk.Label(
        root, 
        text="DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND DATA SCIENCE",
        font=("Times New Roman", 20),
        fg="black",
        bg="yellow"
    )
    label.place(x=screen_width // 2, y=50, anchor="center")

    # Left Frame for Video Feed
    left_frame = tk.Frame(root, bg="white", width=500, height=500)
    left_frame.place(x=135, y=150)

    # Right Frame for Controls
    right_frame = tk.Frame(root, bg="white", width=500, height=500)
    right_frame.place(x=655, y=150)

    # Register Button
    register_button = tk.Button(
        root, 
        text="Register Faces", 
        font=("Times New Roman", 16),
        bg='light pink',
        command=lambda: create_input_fields(right_frame, cap)
    )
    register_button.place(x=screen_width // 2, y=screen_height - 100, anchor="center")

    # Display Attendance Button
    display_button = tk.Button(
        root, 
        text="Display Attendance", 
        font=("Times New Roman", 16),
        bg='light green',
        command=display_attendance_list
    )
    display_button.place(x=screen_width // 2, y=screen_height - 50, anchor="center")

    # Start video capture in the left frame
    capture_video(cap, left_frame)

def create_input_fields(right_frame, cap):
    # Fields for Name and Roll Number
    name_label = tk.Label(right_frame, text="Name:", font=("Times New Roman", 14), bg="white")
    name_label.place(relx=0.2, rely=0.2)
    name_entry = tk.Entry(right_frame, font=("Times New Roman", 14))
    name_entry.place(relx=0.4, rely=0.2)

    roll_no_label = tk.Label(right_frame, text="Roll No:", font=("Times New Roman", 14), bg="white")
    roll_no_label.place(relx=0.2, rely=0.4)
    roll_no_entry = tk.Entry(right_frame, font=("Times New Roman", 14))
    roll_no_entry.place(relx=0.4, rely=0.4)

    enroll_button = tk.Button(
        right_frame, 
        text="Enroll", 
        font=("Times New Roman", 14), 
        bg="orange",
        command=lambda: register_face(name_entry.get(), roll_no_entry.get(), cap)
    )
    enroll_button.place(relx=0.5, rely=0.6, anchor="center")
