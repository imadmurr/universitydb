# faculty_ui.py
import tkinter as tk
import shared.theme as theme
from shared.components.cards import create_card

class UniversityUI:
    def __init__(self, parent_frame):
        # Frame for the Faculty UI screen
        self.frame = tk.Frame(parent_frame, bg=theme.BG_COLOR)

        # Title Label for the Faculty Management screen
        self.title_label = tk.Label(self.frame, text="University Management",
                                    font=("Arial", 20, "bold"), bg=theme.BG_COLOR, fg=theme.SIDEBAR_COLOR)
        self.title_label.pack(pady=20)

        # Card Frame for displaying information about faculties
        self.card_frame = tk.Frame(self.frame, bg=theme.BG_COLOR)
        self.card_frame.pack(pady=20)

        # Create cards for showing some static data
        create_card(self.card_frame, "Total Universities", "12")  # TODO: Replace with dynamic data

        # TODO: Add functionality for displaying a list of universities, adding, editing, or deleting universities.
        # Example of displaying a list of universities (this could be in a treeview, listbox, etc.):
        # self.university_listbox = tk.Listbox(self.frame)
        # self.university_listbox.pack(pady=20)

        # TODO: Add buttons for adding/editing/deleting
        # add_button = tk.Button(self.frame, text="Add University", command=self.add_university)
        # add_button.pack()

        # TODO: Implement any additional UI components for University Management, like search, filters, etc.

    def get_frame(self):
        """Return the frame for this screen to be used by the navigation."""
        return self.frame
