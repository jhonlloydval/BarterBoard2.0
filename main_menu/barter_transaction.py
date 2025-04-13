
import sqlite3
from models.user import *
from clear import clear_terminal
from models.barterboardDB import *

def view_transactions_menu():
    width = 50
    print("\n")
    print(
        """

--------------------------- M E N U ---------------------------
▗▄▄▄▖▗▄▄▖  ▗▄▖ ▗▖  ▗▖ ▗▄▄▖ ▗▄▖  ▗▄▄▖▗▄▄▄▖▗▄▄▄▖ ▗▄▖ ▗▖  ▗▖ ▗▄▄▖
  █  ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌ ▐▌▐▌     █    █  ▐▌ ▐▌▐▛▚▖▐▌▐▌   
  █  ▐▛▀▚▖▐▛▀▜▌▐▌ ▝▜▌ ▝▀▚▖▐▛▀▜▌▐▌     █    █  ▐▌ ▐▌▐▌ ▝▜▌ ▝▀▚▖
  █  ▐▌ ▐▌▐▌ ▐▌▐▌  ▐▌▗▄▄▞▘▐▌ ▐▌▝▚▄▄▖  █  ▗▄█▄▖▝▚▄▞▘▐▌  ▐▌▗▄▄▞▘                                                 
                                                              
------------ REVIVING BARTER, REINVENTING EXCHANGE ------------                                                        
                                                                """.center(width))

    view_transactions()

    return "RETURN_TO_MENU"


def view_transactions():
    """
    Displays all accepted transactions for the user.
    """

    get_username = list(User.get_logged_in_user())
    username = get_username[1]

    conn = setup_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transactions
        WHERE from_user = %s OR to_user = %s
""", (username, username))
    
    transactions = cursor.fetchall()
    print("\nT R A N S A C T I O N S")
    print("----------------------------------------------------")
    if not transactions:
        print("No transactions found.")
        print("----------------------------------------------------")
        conn.close
        input("Press enter to continue.")
        clear_terminal()
        return
    
    for transaction in transactions:
        print(f"\nTransaction ID: {transaction[0]}")
        print(f"From: {transaction[1]} ")
        print(f"To: {transaction[2]}")
        print(f"Item: {transaction[3]}")
        print(f"Description: {transaction[4]}")
        print(f"Quantity: {transaction[5]}")
        print(f"Status: {transaction[6]}")
        print("----------------------------------------------------")

    input("Press enter to exit.")
    clear_terminal()
    conn.close()

