from core.db import Database

class DepartmentService:
    def __init__(self):
        """Initialize the DepartmentService with a database connection."""
        self.db = Database(host="localhost", user="root", password="yourpassword", database="university_db")
        self.db.connect()

    def get_all_departments(self):
        """Fetch all departments from the database."""
        query = "SELECT * FROM departments"
        # TODO: Fetch all departments using the fetch_all method from the db class
        return self.db.fetch_all(query)

    def get_department_by_id(self, department_id):
        """Fetch a department by its ID."""
        query = "SELECT * FROM departments WHERE id = %s"
        # TODO: Fetch a department by its ID using the fetch_one method from the db class
        return self.db.fetch_one(query, (department_id,))

    def add_department(self, name, faculty_id):
        """Add a new department to the database."""
        query = "INSERT INTO departments (name, faculty_id) VALUES (%s, %s)"
        # TODO: Execute the insert query using execute_query method from the db class
        self.db.execute_query(query, (name, faculty_id))

    def update_department(self, department_id, name, faculty_id):
        """Update the details of an existing department."""
        query = "UPDATE departments SET name = %s, faculty_id = %s WHERE id = %s"
        # TODO: Execute the update query using execute_query method from the db class
        self.db.execute_query(query, (name, faculty_id, department_id))

    def delete_department(self, department_id):
        """Delete a department from the database."""
        query = "DELETE FROM departments WHERE id = %s"
        # TODO: Execute the delete query using execute_query method from the db class
        self.db.execute_query(query, (department_id,))

    def __del__(self):
        """Disconnect the database connection when done."""
        self.db.disconnect()
