import os
import csv
from tkinter import Toplevel, Text, Tk, Scrollbar, RIGHT, Y, END, BOTH

def display_attendance_list(file_path):
    """
    Reads a CSV file containing attendance and displays the content in a new Tkinter window.

    :param file_path: Path to the CSV file containing attendance data.
    """
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' does not exist.")
        return

    # Create a new window
    root = Tk()
    root.withdraw()  # Hide the root window
    top = Toplevel()
    top.title("Attendance List")
    top.geometry("600x400")

    # Add a scrolling text widget
    scrollbar = Scrollbar(top)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_widget = Text(top, wrap='none', yscrollcommand=scrollbar.set)
    text_widget.pack(expand=True, fill=BOTH)
    scrollbar.config(command=text_widget.yview)

    try:
        # Read and display CSV content
        with open(file_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                text_widget.insert(END, ', '.join(row) + '\n')

    except Exception as e:
        text_widget.insert(END, f"Error reading the file: {e}\n")

    text_widget.config(state='disabled')  # Make the text widget read-only
    top.mainloop()


# Example usage
if __name__ == "__main__":
    display_attendance_list("attendance.csv")
