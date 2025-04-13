# MAIN MENU

from models.listing import *
from main_menu.barterboard_main import barterboard
from main_menu.barter_transaction import *
from main_menu.view_listing import *
from main_menu.listing_update import *
from main_menu.create_listing import *
from main_menu.bargain import bargain
from clear import clear_terminal

def main_menu():
    
    while True:
        width = 50
        print("\n")
        print(
            """
---------------- M A I N   M E N U ----------------

██████╗  █████╗ ██████╗ ████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║██████╔╝   ██║   █████╗  ██████╔╝
██╔══██╗██╔══██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║  ██║   ██║   ███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

------ REVIVING BARTER, REINVENTING EXCHANGE ------                                                    
                                                    """.center(width))

        print("1) BARTERBOARD\n2) ADD LISTING\n3) VIEW LISTING\n4) LISTING UPDATE\n5) TRANSACTION\n6) EXIT")
        
        menu_choice = input("\nEnter your choice: ")

        if menu_choice == "1":
            clear_terminal()
            result = barterboard()
            if result == "RETURN_TO_MENU":
                continue
            
        elif menu_choice == "2":
            clear_terminal()
            result = create_list()
            if result == "RETURN_TO_MENU":
                continue

        elif menu_choice == "3":
            clear_terminal()
            result = view_list()
            if result == "RETURN_TO_MENU":
                continue

        elif menu_choice == "4":
            clear_terminal()
            result = update_list()
            if result == "RETURN_TO_MENU":
                continue

        elif menu_choice == "5":
            clear_terminal()
            result = view_transactions_menu()
            if result == "RETURN_TO_MENU":
                continue

        elif menu_choice == "6":
            clear_terminal()
            break

        else:
            print("Enter the correct number of your choice.")

    
