# BARTERBOARD SECTION

from models.listing import display_barterboard
from main_menu.bargain import bargain
from models.user import User
from clear import clear_terminal

username = User.get_logged_in_user()

def barterboard():
    width = 50
    print("\n")
    print(
        """

----------------------- M E N U -----------------------
▗▄▄▖  ▗▄▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▄▄▖ ▗▄▄▖  ▗▄▖  ▗▄▖ ▗▄▄▖ ▗▄▄▄  
▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌ █  ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌  █ 
▐▛▀▚▖▐▛▀▜▌▐▛▀▚▖ █  ▐▛▀▀▘▐▛▀▚▖▐▛▀▚▖▐▌ ▐▌▐▛▀▜▌▐▛▀▚▖▐▌  █ 
▐▙▄▞▘▐▌ ▐▌▐▌ ▐▌ █  ▐▙▄▄▖▐▌ ▐▌▐▙▄▞▘▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌▐▙▄▄▀                                                                                                  
                                                        
-------- REVIVING BARTER, REINVENTING EXCHANGE --------  """.center(width))
    
    listings = display_barterboard()
    
    while True:
        print("\n1) BARGAIN\n2) RETURN TO MAIN MENU\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            bargain(username, listings)
        elif choice == "2":
            clear_terminal()
            return "RETURN_TO_MENU"
        else:
            print("Enter the correct number of your choice.")


