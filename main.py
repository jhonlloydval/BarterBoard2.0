from models.user import *
from menu import *
from models.listing import *
from models.transaction import *
from clear import clear_terminal

# Register function
def register():
    print("\nR E G I S T E R  A C C O U N T")
    print("To register, follow the prompts below.\nYou can exit this section at any time by typing 'x.'")
    print("Username and password must be 5-15 characters long.\n")
    
    while True:
        enter_username = input("Enter your username: ")
        if enter_username.lower() == "x":
            clear_terminal()
            return 
        if 5 <= len(enter_username) <= 15:
            break
        print("Username must be 5-15 characters long.")
    
    while True:
        enter_password = input("Enter your password: ")
        if enter_password.lower() == "x":
            clear_terminal()
            return
        if 5 <= len(enter_password) <= 15:
            break
        print("Password must be 5-15 characters long.")
    
    # If upon registering, the username already exists
    while not User.register(enter_username, enter_password):
        print("Please choose a different username.")
        enter_username = input("Enter a new username: ")
        if enter_username.lower() == "x":
            clear_terminal()
            return
    
    # After regisering, it will go back to start menu
    input("\nPress enter return to start menu.")
    clear_terminal()
    return
    
# Login function
def login():
    print("\nL O G I N  A C C O U N T")
    print("To login, follow the prompts below.\nYou can exit this section at any time by typing 'x.'\n")
    
    while True:
        account_username = input("Enter username: ")
        if account_username.lower() == "x":
            clear_terminal()
            return
        account_password = input("Enter password: ")
        if account_password.lower() == "x":
            clear_terminal()
            return
        
        user = User.login(account_username, account_password)
        
        # if user login = True
        if user:
            # Proceed to the next step in your application after login
            clear_terminal()
            main_menu()  
            return
        else:
            print("Wrong account credentials. Please try again.")

# Main menu
def start_menu():
    while True:

        # Base width for centering
        # ASCII art from patorjk.com

        width = 50
        print("\n")
        print(
            """
------------------ WELCOME TO ------------------

██████╗  █████╗ ██████╗ ████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║██████╔╝   ██║   █████╗  ██████╔╝
██╔══██╗██╔══██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██║   ██║   ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

----- REVIVING BARTER, REINVENTING EXCHANGE -----                               
                                                   """.center(width))
        
        print("1) REGISTER\n2) LOGIN\n3) EXIT")

        start_choice = input("\nEnter your choice: ")
        if start_choice == "1":
            register()
        elif start_choice == "2":
            login()
        elif start_choice == "3":
            print("Exiting application. Goodbye!")
            return
        else:
            print("Enter the correct number of your choice.")

# START MENU
start_menu()




# TO BE ADDED FEATURES
# DONE TBA Ung mga ASCII art
# DONE TBA Barter name to be updated. It is currently a place holder.
# TBA I'll make a secret code where if it is ran, I will go to database editor where I can remove users.
# DONE TBA Clears when I enter something.
# DONE TBA bawal gumawa ng proposal sa sariling item
# DONE TBA dapat nasa item 18 kung sa 18 nag proposal
# DONE TBA napunta agad sa main menu pag pumunta me sa listing update
# DONE TBA pag galing sa listing update/ feel ko sa listing update, napunta agad ng barter