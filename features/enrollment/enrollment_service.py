from core.db import Database

class EnrollmentService:
    def __init__(self):
        """Initialize the EnrollmentService with a database connection."""
        self.db = Database(host="localhost", user="root", password="yourpassword", database="university_db")
        self.db.connect()

    def get_all_enrollments(self):
        """Fetch all enrollments from the database."""
        query = "SELECT * FROM enrollments"
        # TODO: Fetch all enrollments using the fetch_all method from the db class
        return self.db.fetch_all(query)

    def get_enrollment_by_id(self, enrollment_id):
        """Fetch an enrollment by its ID."""
        query = "SELECT * FROM enrollments WHERE id = %s"
        # TODO: Fetch an enrollment by its ID using the fetch_one method from the db class
        return self.db.fetch_one(query, (enrollment_id,))

    def add_enrollment(self, student_id, course_id):
        """Add a new enrollment to the database."""
        query = "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)"
        # TODO: Execute the insert query using execute_query method from the db class
        self.db.execute_query(query, (student_id, course_id))

    def update_enrollment(self, enrollment_id, student_id, course_id):
        """Update an enrollment."""
        query = "UPDATE enrollments SET student_id = %s, course_id = %s WHERE id = %s"
        # TODO: Execute the update query using execute_query method from the db class
        self.db.execute_query(query, (student_id, course_id, enrollment_id))

    def delete_enrollment(self, enrollment_id):
        """Delete an enrollment."""
        query = "DELETE FROM enrollments WHERE id = %s"
        # TODO: Execute the delete query using execute_query method from the db class
        self.db.execute_query(query, (enrollment_id,))

    def __del__(self):
        """Disconnect the database connection when done."""
        self.db.disconnect()
