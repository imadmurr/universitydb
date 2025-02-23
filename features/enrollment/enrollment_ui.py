import tkinter as tk
import shared.theme as theme
from shared.components.cards import create_card

class EnrollmentUI:
    def __init__(self, parent_frame):
        # Frame for the Enrollment UI screen
        self.frame = tk.Frame(parent_frame, bg=theme.BG_COLOR)

        # Title Label for the Enrollment Management screen
        self.title_label = tk.Label(self.frame, text="Enrollment Management",
                                    font=("Arial", 20, "bold"), bg=theme.BG_COLOR, fg=theme.SIDEBAR_COLOR)
        self.title_label.pack(pady=20)

        # Card Frame for displaying information about enrollments
        self.card_frame = tk.Frame(self.frame, bg=theme.BG_COLOR)
        self.card_frame.pack(pady=20)

        # Create cards for showing some static data
        create_card(self.card_frame, "Total Enrollments", "2000")  # TODO: Replace with dynamic data

        # TODO: Add functionality for displaying a list of enrollments, adding, editing, or deleting enrollments.
        # Example of displaying a list of enrollments (this could be in a treeview, listbox, etc.):
        # self.enrollment_listbox = tk.Listbox(self.frame)
        # self.enrollment_listbox.pack(pady=20)

        # TODO: Add buttons for adding/editing/deleting enrollments
        # add_button = tk.Button(self.frame, text="Add Enrollment", command=self.add_enrollment)
        # add_button.pack()

        # TODO: Implement any additional UI components for Enrollment Management, like search, filters, etc.

    def get_frame(self):
        """Return the frame for this screen to be used by the navigation."""
        return self.frame
