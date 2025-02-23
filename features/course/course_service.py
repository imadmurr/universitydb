from core.db import Database

class CourseService:
    def __init__(self):
        """Initialize the CourseService with a database connection."""
        self.db = Database(host="localhost", user="root", password="yourpassword", database="university_db")
        self.db.connect()

    def get_all_courses(self):
        """Fetch all courses from the database."""
        query = "SELECT * FROM courses"
        # TODO: Fetch all courses using the fetch_all method from the db class
        return self.db.fetch_all(query)

    def get_course_by_id(self, course_id):
        """Fetch a course by its ID."""
        query = "SELECT * FROM courses WHERE id = %s"
        # TODO: Fetch a course by its ID using the fetch_one method from the db class
        return self.db.fetch_one(query, (course_id,))

    def add_course(self, name, department_id):
        """Add a new course to the database."""
        query = "INSERT INTO courses (name, department_id) VALUES (%s, %s)"
        # TODO: Execute the insert query using execute_query method from the db class
        self.db.execute_query(query, (name, department_id))

    def update_course(self, course_id, name, department_id):
        """Update the details of an existing course."""
        query = "UPDATE courses SET name = %s, department_id = %s WHERE id = %s"
        # TODO: Execute the update query using execute_query method from the db class
        self.db.execute_query(query, (name, department_id, course_id))

    def delete_course(self, course_id):
        """Delete a course from the database."""
        query = "DELETE FROM courses WHERE id = %s"
        # TODO: Execute the delete query using execute_query method from the db class
        self.db.execute_query(query, (course_id,))

    def __del__(self):
        """Disconnect the database connection when done."""
        self.db.disconnect()
