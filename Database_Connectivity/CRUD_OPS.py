import mysql.connector
from mysql.connector import Error

def connect_db():
    """Establish connection to MySQL"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # your username
            password="root",    # your password
            database="24_python_gen"    # your database name
        )

        if connection.is_connected():
            version_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server Version {version_info}")
            return connection
        
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def create_user(name, email, age, country):
    connection = connect_db()
    if connection is None:
        return "Connection failed."
    
    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (name, email, age, country) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, age, country))
        connection.commit()
        print(f"User {name} added successfully.")
    except Error as e:
        print(f"Failed to add user {name}: {e}")
        connection.rollback()
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def read_users():
    connection = connect_db()
    if connection is None:
        return "Connection failed."
    
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        if users:
            for user in users:
                print(user)
        else:
            print("No users found.")
    except Error as e:
        print(f"Failed to read users: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_user(user_id, name=None, email=None, age=None):
    pass

def delete_user(user_id):
    connection = connect_db()
    if connection is None:
        return "Connection failed."
    
    try:
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        if cursor.rowcount == 0:
            print(f"No user with ID {user_id} found.")
        else:
            print(f"User ID {user_id} deleted successfully.")
    except Error as e:
        print(f"Failed to delete user {user_id}: {e}")
        connection.rollback()
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def menu():
    while True:
        print("\n-- CRUD Menu ---")
        print("1. Create User")
        print("2. Read All User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        match choice:
            case 1:
                name = input("Enter name: ")
                email = input("Enter email: ")
                try:
                    age = int(input("Enter age: "))
                except ValueError:
                    print("Invalid age! Please enter a valid number.")
                    continue
                country = input("Enter country: ")
                create_user(name, email, age, country)

            case 2:
                print("\nAll Users:")
                read_users()

            case 3:
                print("Soon!")

            case 4:
                try:
                    user_id = int(input("Enter user ID to delete: "))
                except ValueError:
                    print("Invalid user ID! Please enter a valid number.")
                    continue

                delete_user(user_id)

            case 5:
                print("Exiting Program...")
                break

            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()