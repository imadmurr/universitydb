from core.db import Database

class FacultyService:
    def __init__(self):
        """Initialize the FacultyService with a database connection."""
        self.db = Database(host="localhost", user="root", password="yourpassword", database="university_db")
        self.db.connect()

    def get_all_faculties(self):
        """Fetch all faculties from the database."""
        query = "SELECT * FROM faculties"
        # TODO: Fetch all faculties using the fetch_all method from the db class
        return self.db.fetch_all(query)

    def get_faculty_by_id(self, faculty_id):
        """Fetch a faculty by its ID."""
        query = "SELECT * FROM faculties WHERE id = %s"
        # TODO: Fetch a faculty by its ID using the fetch_one method from the db class
        return self.db.fetch_one(query, (faculty_id,))

    def add_faculty(self, name, university_id):
        """Add a new faculty to the database."""
        query = "INSERT INTO faculties (name, university_id) VALUES (%s, %s)"
        # TODO: Execute the insert query using execute_query method from the db class
        self.db.execute_query(query, (name, university_id))

    def update_faculty(self, faculty_id, name, university_id):
        """Update the details of an existing faculty."""
        query = "UPDATE faculties SET name = %s, university_id = %s WHERE id = %s"
        # TODO: Execute the update query using execute_query method from the db class
        self.db.execute_query(query, (name, university_id, faculty_id))

    def delete_faculty(self, faculty_id):
        """Delete a faculty from the database."""
        query = "DELETE FROM faculties WHERE id = %s"
        # TODO: Execute the delete query using execute_query method from the db class
        self.db.execute_query(query, (faculty_id,))

    def __del__(self):
        """Disconnect the database connection when done."""
        self.db.disconnect()
