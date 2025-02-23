from core.db import Database

class StudentService:
    def __init__(self):
        """Initialize the StudentService with a database connection."""
        self.db = Database(host="localhost", user="root", password="yourpassword", database="university_db")
        self.db.connect()

    def get_all_students(self):
        """Fetch all students from the database."""
        query = "SELECT * FROM students"
        # TODO: Fetch all students using the fetch_all method from the db class
        return self.db.fetch_all(query)

    def get_student_by_id(self, student_id):
        """Fetch a student by its ID."""
        query = "SELECT * FROM students WHERE id = %s"
        # TODO: Fetch a student by its ID using the fetch_one method from the db class
        return self.db.fetch_one(query, (student_id,))

    def add_student(self, name, department_id, enrollment_year):
        """Add a new student to the database."""
        query = "INSERT INTO students (name, department_id, enrollment_year) VALUES (%s, %s, %s)"
        # TODO: Execute the insert query using execute_query method from the db class
        self.db.execute_query(query, (name, department_id, enrollment_year))

    def update_student(self, student_id, name, department_id, enrollment_year):
        """Update the details of an existing student."""
        query = "UPDATE students SET name = %s, department_id = %s, enrollment_year = %s WHERE id = %s"
        # TODO: Execute the update query using execute_query method from the db class
        self.db.execute_query(query, (name, department_id, enrollment_year, student_id))

    def delete_student(self, student_id):
        """Delete a student from the database."""
        query = "DELETE FROM students WHERE id = %s"
        # TODO: Execute the delete query using execute_query method from the db class
        self.db.execute_query(query, (student_id,))

    def __del__(self):
        """Disconnect the database connection when done."""
        self.db.disconnect()
