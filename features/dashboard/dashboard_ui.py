import tkinter as tk
from shared.components.cards import create_card
import shared.theme as theme
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class HomeUI:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg=theme.BG_COLOR)

        # Home Screen Title
        title_label = tk.Label(self.frame, text="University Management System",
                               font=("Arial", 20, "bold"), bg=theme.BG_COLOR, fg=theme.SIDEBAR_COLOR)
        title_label.pack(pady=20)

        # Home Screen Content with Cards
        card_frame = tk.Frame(self.frame, bg=theme.BG_COLOR)
        card_frame.pack(pady=20)

        # Dashboard Cards (using a frame for each card)
        create_card(card_frame, "Total Students", "1500")
        create_card(card_frame, "Active Courses", "45")
        create_card(card_frame, "Departments", "12")
        create_card(card_frame, "Instructors", "50")

        # Frame for Charts (Using grid for layout)
        chart_frame = tk.Frame(self.frame, bg=theme.BG_COLOR)
        chart_frame.pack(pady=20)

        # Create Pie and Bar charts next to each other using grid
        self.create_pie_chart(chart_frame)
        self.create_bar_chart(chart_frame)

    def create_pie_chart(self, parent):
        """Creates a pie chart showing department distribution"""
        fig, ax = plt.subplots(figsize=(4, 3))
        labels = ['CS', 'Maths', 'Engineering', 'Chemistry']
        sizes = [40, 30, 20, 10]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#99ff99', '#ff6666', '#ffcc99'])
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)  # Place pie chart in first grid column

    def create_bar_chart(self, parent):
        """Creates a bar chart showing number of students in each faculty"""
        fig, ax = plt.subplots(figsize=(3, 3))
        faculties = ['CS', 'Maths', 'Eng', 'Arts']
        students = [500, 300, 200, 100]
        ax.bar(faculties, students, color='#66b3ff')
        ax.set_ylabel('Number of Students')
        ax.set_title('Students per Faculty')

        # Embed the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=1, padx=10, pady=10)  # Place bar chart in second grid column

    def get_frame(self):
        return self.frame
