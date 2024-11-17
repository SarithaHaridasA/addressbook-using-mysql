import mysql.connector
from mysql.connector import Error

class DatabaseOperations:

    connection = None

    def __init__(self):
        self.connect_database()

    def connect_database(self):
        try:
            # Connect to MySQL server
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='eusjsk',
                database = "address_book_management"
            )
            if self.connection.is_connected():
                print("Connected to MySQL server")

        except Error as e:
            print(f"Error: {e}")

    def check_database_connected(self):
        try:
            if self.connection.is_connected():
                print('database connected')
            else:
                print('database not connected')
        except Error as e:
            print(f"Error: {e}")

    def save_data(self, data, tableName):
        try:
            cursor = self.connection.cursor()
            # Construct the SQL query
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {tableName} ({columns}) VALUES ({placeholders})"

            # Execute the query
            cursor.execute(query, tuple(data.values()))
            self.connection.commit()  # Commit the transaction
            print("Data inserted successfully.")
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def search_values_from_contacts(self, search_value):
        try:
            cursor = self.connection.cursor(dictionary=True)
            # Construct the SQL query
            query = f"""
                SELECT * FROM contacts
                WHERE first_name LIKE %s OR phone LIKE %s OR email LIKE %s
                """
            search_pattern = f"%{search_value}%"
            # Execute the query
            cursor.execute(query, (search_pattern, search_pattern, search_pattern))
            results = cursor.fetchall()  # Fetch all matching rows
            print(f"Found {len(results)} result(s).")
            return results
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def fetch_all_values(self, table_name):
        try:
            cursor = self.connection.cursor(dictionary=True)
            # Construct the SQL query
            query = f"""
                SELECT * FROM {table_name}
                """
            # Execute the query
            cursor.execute(query)
            results = cursor.fetchall()  # Fetch all matching rows
            print(f"Found {len(results)} result(s).")
            return results
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []


