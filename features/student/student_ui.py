import tkinter as tk
import shared.theme as theme
from shared.components.cards import create_card

class StudentUI:
    def __init__(self, parent_frame):
        # Frame for the Student UI screen
        self.frame = tk.Frame(parent_frame, bg=theme.BG_COLOR)

        # Title Label for the Student Management screen
        self.title_label = tk.Label(self.frame, text="Student Management",
                                    font=("Arial", 20, "bold"), bg=theme.BG_COLOR, fg=theme.SIDEBAR_COLOR)
        self.title_label.pack(pady=20)

        # Card Frame for displaying information about students
        self.card_frame = tk.Frame(self.frame, bg=theme.BG_COLOR)
        self.card_frame.pack(pady=20)

        # Create cards for showing some static data
        create_card(self.card_frame, "Total Students", "1500")  # TODO: Replace with dynamic data

        # TODO: Add functionality for displaying a list of students, adding, editing, or deleting students.
        # Example of displaying a list of students (this could be in a treeview, listbox, etc.):
        # self.student_listbox = tk.Listbox(self.frame)
        # self.student_listbox.pack(pady=20)

        # TODO: Add buttons for adding/editing/deleting students
        # add_button = tk.Button(self.frame, text="Add Student", command=self.add_student)
        # add_button.pack()

        # TODO: Implement any additional UI components for Student Management, like search, filters, etc.

    def get_frame(self):
        """Return the frame for this screen to be used by the navigation."""
        return self.frame
