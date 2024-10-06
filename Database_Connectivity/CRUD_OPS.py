import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection

def connect_db() -> MySQLConnection:
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

def create_user(name, email, age, country) -> None:
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

def read_users() -> None:
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

def update_user(user_id: int, new_name: str=None, new_email: str=None, new_age=None, new_country: str=None) -> None:

    connection = connect_db()
    if connection is None:
        return "Connection failed."
    
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        users = cursor.fetchone()
        if users:
            name = users[1]
            email = users[2]
            age = users[3]
            country = users[4]

            if (new_name != None):
                name = new_name
            if (new_email != None):
                email = new_email
            if (new_age != None):
                age = new_age
            if (new_country != None):
                country = new_country
            
            query = "UPDATE users SET name=%s, email=%s, age=%s, country=%s WHERE id=%s"
            cursor.execute(query, (name, email, age, country, user_id,))
            connection.commit()
        else:
            print("No users found.")
    except Error as e:
        print(f"Failed to update user: {e}")
        connection.rollback()
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_user_by_id(user_id: int):
    connection = connect_db()
    if connection is None:
        return "Connection failed."
    
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        users = cursor.fetchone()
        if users:
            print(users)
        else:
            print("No users found.")
    except Error as e:
        print(f"Failed to update user: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

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
        print("5. GetUserById")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

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
                try:
                    user_id = int(input("Enter user ID to update: "))
                    name = input("Enter a new name or press '-' to skip: ")
                    email = input("Enter a new email or press '-' to skip: ")
                    age = input("Enter a new age or press '-' to skip: ")
                    country = input("Enter a new country or press '-' to skip: ")
                except ValueError:
                    print("Invalid Data! Please enter valid data.")
                    continue

                if name == '-':
                    name = None
                if email == '-':
                    email = None
                if age == '-':
                    age = None
                if country == '-':
                    country = None

                update_user(user_id, name, email, age, country)

            case 4:
                try:
                    user_id = int(input("Enter user ID to delete: "))
                except ValueError:
                    print("Invalid user ID! Please enter a valid number.")
                    continue

                delete_user(user_id)

            case 5:
                try:
                    user_id = int(input("Enter user ID to get the user details: "))
                except ValueError:
                    print("Invalid user ID! Please enter a valid number.")
                    continue

                get_user_by_id(user_id)

            case 6:
                print("Exiting Program...")
                break

            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    menu()