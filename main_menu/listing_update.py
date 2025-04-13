
# CREATE LISTING
from models.user import User
from models.listing import *

def update_list():
    logged_in_user = User.get_logged_in_user()
    username = logged_in_user[1]

    width = 50
    print("\n")
    print("""
------------------------------- M E N U -------------------------------
▗▖   ▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖    ▗▖ ▗▖▗▄▄▖ ▗▄▄▄   ▗▄▖▗▄▄▄▖▗▄▄▄▖
▐▌     █  ▐▌     █    █  ▐▛▚▖▐▌▐▌       ▐▌ ▐▌▐▌ ▐▌▐▌  █ ▐▌ ▐▌ █  ▐▌   
▐▌     █   ▝▀▚▖  █    █  ▐▌ ▝▜▌▐▌▝▜▌    ▐▌ ▐▌▐▛▀▘ ▐▌  █ ▐▛▀▜▌ █  ▐▛▀▀▘
▐▙▄▄▖▗▄█▄▖▗▄▄▞▘  █  ▗▄█▄▖▐▌  ▐▌▝▚▄▞▘    ▝▚▄▞▘▐▌   ▐▙▄▄▀ ▐▌ ▐▌ █  ▐▙▄▄▖
          
---------------- REVIVING BARTER, REINVENTING EXCHANGE ----------------                                                                                                                 
                                                                        """.center(width))
    
    
    # Create a Listing object
    listing = Listing(username)

    # Call the method from the Listing class
    listing.update_listing()

