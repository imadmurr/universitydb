import mysql.connector
from mysql.connector import Error

# Example usage:

#     db = Database(host="localhost", user="root", password="yourpassword", database="university_db")
#     db.connect()

#     # Example of inserting data
#     insert_sql = "INSERT INTO universities (name, location) VALUES (%s, %s)"
#     db.execute_query(insert_sql, ("University A", "City X"))

#     # Example of fetching data
#     universities = db.fetch_all("SELECT * FROM universities")
#     print(universities)

#     db.disconnect()
class Database:
    def __init__(self, host, user, password, database):
        """Initialize the database connection with MySQL."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Create a database connection to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print(f"Successfully connected to {self.database} database on {self.host}")
        except Error as e:
            print(f"Error: {e}")

    def disconnect(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

    def execute_query(self, query, params=()):
        """Execute a single query without returning results (e.g., INSERT, UPDATE, DELETE)."""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")

    def fetch_one(self, query, params=()):
        """Fetch a single record from the database."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Error as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_all(self, query, params=()):
        """Fetch all records from the database."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error executing query: {e}")
            return []

    def create_table(self, create_table_sql):
        """Create a table in the database."""
        try:
            self.cursor.execute(create_table_sql)
            self.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")


