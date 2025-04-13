# CREATE LISTING
from models.user import User
from models.listing import *

def view_list():
    logged_in_user = User.get_logged_in_user()
    username = logged_in_user[1]

    width = 50
    print("\n")
    print("""
          
-------------------------- M E N U --------------------------
▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▖ ▗▖    ▗▖   ▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖
▐▌  ▐▌  █  ▐▌   ▐▌ ▐▌    ▐▌     █  ▐▌     █    █  ▐▛▚▖▐▌▐▌   
▐▌  ▐▌  █  ▐▛▀▀▘▐▌ ▐▌    ▐▌     █   ▝▀▚▖  █    █  ▐▌ ▝▜▌▐▌▝▜▌
 ▝▚▞▘ ▗▄█▄▖▐▙▄▄▖▐▙█▟▌    ▐▙▄▄▖▗▄█▄▖▗▄▄▞▘  █  ▗▄█▄▖▐▌  ▐▌▝▚▄▞▘
          
----------- REVIVING BARTER, REINVENTING EXCHANGE -----------                                                      
                                                                """.center(width))
    print("Note: Type 'x' to exit at any time.")

    # Create a Listing object
    listing = Listing(username)

    # Call the method from the Listing class
    listing.view_own_listings()

