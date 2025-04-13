# THE USER CLASS
from models.barterboardDB import *
from mysql.connector import errorcode, errors

current_user = None

class User:
    def __init__(self, username, password):
        """ Initialize the User object with a username and password. """
        self.username = username
        self.password = password

    @staticmethod
    def register(username, password):
        """ Registers a new user in the database. """
        conn = setup_database()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            print("Account successfully created!")
            return True
        except errors.IntegrityError as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("Username already exists. Please try again.")
            else:
                print("Database error:", err)
            return False
        finally:
            conn.close()

    @staticmethod
    def login(username, password):
        """Checks user credentials in the database."""
        conn = setup_database()
        global current_user
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            current_user = user
            print(f"Logged in as {username}")
            return True
        else:
            print("Invalid username or password.")
            return False
    
    @staticmethod
    def get_logged_in_user():
        """Returns the logged-in user if available"""
        return current_user
    
        