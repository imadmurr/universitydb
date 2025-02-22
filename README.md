# University Database Management System

## Overview
The **University Database Management System** is a desktop application built using **Tkinter** and **MySQL**. It allows users to manage university-related data, including students, faculties, courses, instructors, and enrollments. The application follows a **modular architecture** and includes a collapsible sidebar for easy navigation.

## Features
- **Dashboard** displaying key statistics and charts
- **University, Faculty, Department, and Course Management**
- **Student and Instructor Management**
- **Enrollment Management**
- **Dynamic UI Components** with cards and charts
- **Collapsible Sidebar Navigation**
- **Modular Code Structure** for better maintainability

## Tech Stack
- **Python (Tkinter)** - for UI development
- **MySQL** - for database management
- **Matplotlib** - for generating charts and graphs

## Installation

### Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **MySQL Server**
- **pip** (Python package manager)

### Clone the Repository
```sh
git clone https://github.com/yourusername/university-db-system.git
cd university-db-system
```

### Install Required Dependencies
```sh
pip install -r requirements.txt
```

### Configure MySQL Database
Import the .sql file

## Project Structure
```
├── core/
│   ├── db.py              # Database connection
│   ├── config.py          # Global configuration
│
├── shared/
│   ├── theme.py           # UI theme settings
│   ├── components/
│   │   ├── cards.py       # Card UI component
│
├── features/
│   ├── university_ui.py   # University management UI
│   ├── faculty_ui.py      # Faculty management UI
│   ├── department_ui.py   # Department management UI
│   ├── instructor_ui.py   # Instructor management UI
│   ├── course_ui.py       # Course management UI
│   ├── student_ui.py      # Student management UI
│   ├── enrollment_ui.py   # Enrollment management UI
│
├── services/
│   ├── university_service.py  # University-related logic
│   ├── faculty_service.py     # Faculty-related logic
│   ├── department_service.py  # Department-related logic
│   ├── instructor_service.py  # Instructor-related logic
│   ├── course_service.py      # Course-related logic
│   ├── student_service.py     # Student-related logic
│   ├── enrollment_service.py  # Enrollment-related logic
│
├── main.py               # Main entry point of the application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```



