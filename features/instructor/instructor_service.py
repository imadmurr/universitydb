from core.db import Database

class InstructorService:
    def __init__(self):
        """Initialize the InstructorService with a database connection."""
        self.db = Database(host="localhost", user="root", password="yourpassword", database="university_db")
        self.db.connect()

    def get_all_instructors(self):
        """Fetch all instructors from the database."""
        query = "SELECT * FROM instructors"
        # TODO: Fetch all instructors using the fetch_all method from the db class
        return self.db.fetch_all(query)

    def get_instructor_by_id(self, instructor_id):
        """Fetch an instructor by its ID."""
        query = "SELECT * FROM instructors WHERE id = %s"
        # TODO: Fetch an instructor by its ID using the fetch_one method from the db class
        return self.db.fetch_one(query, (instructor_id,))

    def add_instructor(self, name, department_id):
        """Add a new instructor to the database."""
        query = "INSERT INTO instructors (name, department_id) VALUES (%s, %s)"
        # TODO: Execute the insert query using execute_query method from the db class
        self.db.execute_query(query, (name, department_id))

    def update_instructor(self, instructor_id, name, department_id):
        """Update the details of an existing instructor."""
        query = "UPDATE instructors SET name = %s, department_id = %s WHERE id = %s"
        # TODO: Execute the update query using execute_query method from the db class
        self.db.execute_query(query, (name, department_id, instructor_id))

    def delete_instructor(self, instructor_id):
        """Delete an instructor from the database."""
        query = "DELETE FROM instructors WHERE id = %s"
        # TODO: Execute the delete query using execute_query method from the db class
        self.db.execute_query(query, (instructor_id,))

    def __del__(self):
        """Disconnect the database connection when done."""
        self.db.disconnect()
