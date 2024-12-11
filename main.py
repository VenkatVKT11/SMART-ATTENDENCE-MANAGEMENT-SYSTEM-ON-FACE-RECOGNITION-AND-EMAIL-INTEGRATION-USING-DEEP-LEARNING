import tkinter as tk
from gui import setup_gui
from face_recognition import init_camera

# Initialize camera
cap = init_camera()

# Create main Tkinter window
root = tk.Tk()
root.title("Attendance Marking Management System")
root.configure(bg="orange")

# Set the window size to full screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Setup GUI components
setup_gui(root, cap)

# Run the main event loop
root.mainloop()
