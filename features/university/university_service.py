from core.db import Database

class UniversityService:
    def __init__(self):
        """Initialize the UniversityService with a database connection."""
        self.db = Database(host="localhost", user="root", password="yourpassword", database="university_db")
        self.db.connect()

    def get_all_universities(self):
        """Fetch all universities from the database."""
        query = "SELECT * FROM universities"
        # TODO: Fetch all universities using the fetch_all method from the db class
        return self.db.fetch_all(query)

    def get_university_by_id(self, university_id):
        """Fetch a university by its ID."""
        query = "SELECT * FROM universities WHERE id = %s"
        # TODO: Fetch a university by its ID using the fetch_one method from the db class
        return self.db.fetch_one(query, (university_id,))

    def add_university(self, name, location):
        """Add a new university to the database."""
        query = "INSERT INTO universities (name, location) VALUES (%s, %s)"
        # TODO: Execute the insert query using execute_query method from the db class
        self.db.execute_query(query, (name, location))

    def update_university(self, university_id, name, location):
        """Update the details of an existing university."""
        query = "UPDATE universities SET name = %s, location = %s WHERE id = %s"
        # TODO: Execute the update query using execute_query method from the db class
        self.db.execute_query(query, (name, location, university_id))

    def delete_university(self, university_id):
        """Delete a university from the database."""
        query = "DELETE FROM universities WHERE id = %s"
        # TODO: Execute the delete query using execute_query method from the db class
        self.db.execute_query(query, (university_id,))

    def __del__(self):
        """Disconnect the database connection when done."""
        self.db.disconnect()
