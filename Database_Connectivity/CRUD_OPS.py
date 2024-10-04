import mysql.connector
from mysql.connector import Error

def connect_db():
    """Establish connection to MySQL"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # your username
            password="root",    # your password
            database="users"    # your database name
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server Version {db_info}")
            return connection
        
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

if __name__ == "__main__":
    # Test the connection
    connection = connect_db()

    # Close the connection if it was established
    if connection is not None and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")