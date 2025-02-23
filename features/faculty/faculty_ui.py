# faculty_ui.py
import tkinter as tk
import shared.theme as theme
from shared.components.cards import create_card

class FacultyUI:
    def __init__(self, parent_frame):
        # Frame for the Faculty UI screen
        self.frame = tk.Frame(parent_frame, bg=theme.BG_COLOR)

        # Title Label for the Faculty Management screen
        self.title_label = tk.Label(self.frame, text="Faculty Management",
                                    font=("Arial", 20, "bold"), bg=theme.BG_COLOR, fg=theme.SIDEBAR_COLOR)
        self.title_label.pack(pady=20)

        # Card Frame for displaying information about faculties
        self.card_frame = tk.Frame(self.frame, bg=theme.BG_COLOR)
        self.card_frame.pack(pady=20)

        # Create cards for showing some static data
        create_card(self.card_frame, "Total Faculties", "12")  # TODO: Replace with dynamic data
        create_card(self.card_frame, "Active Courses", "35")  # TODO: Replace with dynamic data

        # TODO: Add functionality for displaying a list of faculties, adding, editing, or deleting faculties.
        # Example of displaying a list of faculties (this could be in a treeview, listbox, etc.):
        # self.faculty_listbox = tk.Listbox(self.frame)
        # self.faculty_listbox.pack(pady=20)

        # TODO: Add buttons for adding/editing/deleting faculties
        # add_button = tk.Button(self.frame, text="Add Faculty", command=self.add_faculty)
        # add_button.pack()

        # TODO: Implement any additional UI components for Faculty Management, like search, filters, etc.

    def get_frame(self):
        """Return the frame for this screen to be used by the navigation."""
        return self.frame
