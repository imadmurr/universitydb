import tkinter as tk
import shared.theme as theme
from core.navigation import Navigation
from features.course.course_ui import CourseUI
from features.dashboard.dashboard_ui import DashboardUI
from features.department.department_ui import DepartmentUI
from features.enrollment.enrollment_ui import EnrollmentUI
from features.faculty.faculty_ui import FacultyUI
from features.instructor.instructor_ui import InstructorUI
from features.student.student_ui import StudentUI
from features.university.university_ui import UniversityUI


class UniversityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University Database Management System")
        self.root.geometry("1024x748")
        self.root.config(bg=theme.BG_COLOR)

        # Create the navigation handler (in the main file)
        self.frames = {}

        # Sidebar Frame (Collapsible)
        self.sidebar_frame = tk.Frame(root, bg=theme.SIDEBAR_COLOR, width=60)
        self.sidebar_frame.pack(side="left", fill="y")

        # Expand/Collapse Button
        self.expand_button = tk.Button(self.sidebar_frame, text="☰", font=("Arial", 16), bg=theme.SIDEBAR_COLOR,
                                       fg=theme.TEXT_COLOR, command=self.toggle_sidebar, relief="flat", cursor="hand2")
        self.expand_button.pack(pady=10, padx=10)

        # Sidebar Buttons
        self.sidebar_buttons = [
            ("🏠 Home", lambda: self.navigation.show_screen('dashboard')),
            ("🏛 Universities", lambda: self.navigation.show_screen('university')),
            ("🏫 Faculties", lambda: self.navigation.show_screen('faculty')),
            ("📖 Departments", lambda: self.navigation.show_screen('department')),
            ("👨‍🏫 Instructors", lambda: self.navigation.show_screen('instructor')),
            ("📚 Courses", lambda: self.navigation.show_screen('course')),
            ("🎓 Students", lambda: self.navigation.show_screen('student')),
            ("📝 Enrollments", lambda: self.navigation.show_screen('enrollment'))
        ]

        self.buttons = []
        for text, command in self.sidebar_buttons:
            btn = tk.Button(self.sidebar_frame, text=text, font=("Arial", 12, "bold"),
                            bg=theme.SIDEBAR_COLOR, fg=theme.TEXT_COLOR, relief="flat", command=command, anchor="w",
                            padx=10, width=18, cursor="hand2")
            btn.pack(pady=5, fill="x")
            self.buttons.append(btn)

        # Main Content Frame
        self.main_frame = tk.Frame(root, bg=theme.BG_COLOR)
        self.main_frame.pack(side="right", expand=True, fill="both")

        # Create frames for each screen (instance of the screen class)
        self.frames['dashboard'] = DashboardUI(self.main_frame).get_frame()
        self.frames['university'] = UniversityUI(self.main_frame).get_frame()
        self.frames['faculty'] = FacultyUI(self.main_frame).get_frame()
        self.frames['department'] = DepartmentUI(self.main_frame).get_frame()
        self.frames['instructor'] = InstructorUI(self.main_frame).get_frame()
        self.frames['course'] = CourseUI(self.main_frame).get_frame()
        self.frames['student'] = StudentUI(self.main_frame).get_frame()
        self.frames['enrollment'] = EnrollmentUI(self.main_frame).get_frame()


        # Initialize navigation
        self.navigation = Navigation(self.root, self.frames)

        # Show the default screen (main screen with dashboard and cards)
        self.navigation.show_screen('dashboard')

    def toggle_sidebar(self):
        """Expands or collapses the sidebar"""
        if self.sidebar_frame.winfo_width() > 60:
            self.sidebar_frame.config(width=60)
            for btn in self.buttons:
                btn.pack_forget()  # Hide buttons
        else:
            self.sidebar_frame.config(width=200)
            for btn in self.buttons:
                btn.pack(pady=5, fill="x")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = UniversityApp(root)
    root.mainloop()
