from models.user import *
from models.barterboardDB import *
from clear import clear_terminal
from main_menu.bargain import accept_trade

def display_barterboard():
    print("\nBARTERBOARD - Available Items for Trade")
    print("----------------------------------------------------")
    conn = setup_database()
    cursor = conn.cursor()

    # Query all listings with their ID
    cursor.execute("""
        SELECT l.id, l.item, l.description, l.quantity, l.location, l.desired_barter, u.username
        FROM listings l
        INNER JOIN users u ON l.user_id = u.id
    """)
    
    results = cursor.fetchall()

    listings = []  # To store processed listings

    if results:
        for idx, (item_id, item, description, quantity, location, desired_barter, username) in enumerate(results, start=1):
            listing = {
                "id": item_id,
                "item": item,
                "description": description,
                "quantity": quantity,
                "location": location,
                "desired_barter": desired_barter,
                "username": username,
            }
            listings.append(listing)
            
            print(f"{idx}. ID: {item_id}")
            print(f"   Item: {item}")
            print(f"   Description: {description}")
            print(f"   Quantity: {quantity}")
            print(f"   Location: {location}")
            print(f"   Desired Barter Item: {desired_barter}")
            print(f"   Listed by: {username}")
            print("----------------------------------------------------")
    else:
        print("No items available for trade at the moment.")
        print("----------------------------------------------------")
    
    conn.close()
    return listings

class Listing:
    def __init__(self, username):
        self.username = username

    def edit_listing(self):
        print("\nE D I T  L I S T I N G")
        print("Select the ID of the listing you want to edit:")
        print("----------------------------------------------------")
        conn = setup_database()
        cursor = conn.cursor()


        cursor.execute("""
            SELECT l.id, l.item
            FROM listings l
            INNER JOIN users u ON l.user_id = u.id
            WHERE u.username = %s
        """, (self.username,))
        listings = cursor.fetchall()

        if not listings:
            print("No listings available to edit.")
            print("----------------------------------------------------")
            conn.close()
            return

        for listing_id, item in listings:
            print(f"ID {listing_id} | Item name: {item}")
        print("----------------------------------------------------")

        while True:
            listing_id = input("Enter ID (Type 'x' to exit): ")
            if listing_id.lower() == 'x':
                conn.close()
                return
            
            if listing_id.isdigit():
                listing_id = int(listing_id)
                cursor.execute("SELECT * FROM listings WHERE id = %s AND user_id = (SELECT id FROM users WHERE username = %s)", (listing_id, self.username))
                if cursor.fetchone():
                    break
                else:
                    print("ID not found. Please try again.")
            else:
                print("Invalid input. Enter a numeric ID or 'x' to exit.")    

        # Fetch the current listing details
        cursor.execute("SELECT item, description, quantity, location, desired_barter FROM listings WHERE id = %s", (listing_id,))
        current_data = cursor.fetchone()
        item, description, quantity, location, desired_barter = current_data

        print("\nLeave blank to keep the current content:\n")
        new_item = input(f"Enter new name (Current: {item}): ") or item
        new_description = input(f"Enter new description (Current: {description}): ") or description
        while True:
            new_quantity = input(f"Enter new quantity (Current: {quantity}): ") or str(quantity)
            if new_quantity.isdigit() and int(new_quantity) > 0:
                new_quantity = int(new_quantity)
                break
            print("Quantity must be a positive number.")

        new_location = input(f"Enter new pickup location (Current: {location}): ") or location
        new_barter = input(f"Enter new desired trade (Current: {desired_barter}): ") or desired_barter

        # Confirm update
        while True:
            confirm = input("Do you want to update? Enter '1' for Yes or '2' for No: ").strip()
            if confirm == "1":
                # Update the database
                cursor.execute("""
                    UPDATE listings
                    SET item = %s, description = %s, quantity = %s, location = %s, desired_barter = %s
                    WHERE id = %s
                """, (new_item, new_description, new_quantity, new_location, new_barter, listing_id))
                conn.commit()
                print(f"Listing ID {listing_id} updated successfully!\n")
                break
            elif confirm == "2":
                print("No changes were made.")
                break
            else:
                print("Enter the correct number of your choice.")

        conn.close()



    def save_to_database(self, item, description, quantity, location, desired_barter):
        conn = setup_database()
        cursor = conn.cursor()

        # Dito makukuha ung USER ID basta 
        cursor.execute("SELECT id FROM users WHERE username = %s", (self.username,))
        user = cursor.fetchone()
        if user:
            user_id = user[0]  # Extract the user ID
            cursor.execute("""
                INSERT INTO listings (user_id, item, description, quantity, location, desired_barter)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (user_id, item, description, quantity, location, desired_barter))
            conn.commit()
            print("Listing created successfully!")
        else:
            print("Error: User not found in the database.")
        
        conn.close()

    def create_listing(self):
         
        while True:
            item = input("\nEnter item name: ")
            if item.lower() == 'x':
                clear_terminal()
                return
            if len(item) > 3:
                break
            print("Name must be longer than 3 characters.")
                
        while True:
            description = input("Enter item description: ")
            if description.lower() == 'x':
                clear_terminal()
                return
            if len(description) > 5:
                break
            print("Description must be longer than 5 characters.")
        
        while True:
            quantity = input("Enter item quantity: ")
            if quantity.lower() == 'x':
                clear_terminal()
                return
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                break
            print("Quantity must be a positive number.")        

        while True:
            location = input("Enter pickup location: ")
            if location.lower() == 'x':
                clear_terminal()
                return
            if len(location) > 3:
                break
            print("Location must be longer than 3 characters.")

        while True:
            barter = input("Enter your desired barter item: ")
            if barter.lower() == 'x':
                clear_terminal()
                return
            if len(barter) > 3:
                break
            print("Barter item name must be longer than 3 characters.")
        
        # Save to database
        print("\n")
        self.save_to_database(item, description, quantity, location, barter)

        while True:
            again = input("Would you like to create another listing?\nEnter '1' to continue or '2' to return to the main menu: ")
            
            if again == "1":
                print("\nC R E A T E  A N O T H E R  L I S T I N G")
                break
            elif again == "2":
                clear_terminal()
                return "RETURN_TO_MENU"
            else:
                print("Enter the correct number of your choice.")
        
        self.create_listing()



    def remove_listing(self):
        print("\nR E M O V E  L I S T I N G")
        print("Select the ID of the listing you want to remove:")
        print("----------------------------------------------------")
        conn = setup_database()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT l.id, l.item
            FROM listings l
            INNER JOIN users u ON l.user_id = u.id
            WHERE u.username = %s
        """, (self.username,))
        listings = cursor.fetchall()

        if not listings:
            print("No listings available to remove.")
            print("----------------------------------------------------")
            conn.close()
            return

        for listing_id, item in listings:
            print(f"ID {listing_id} | Item name: {item}")
        print("----------------------------------------------------")
        print("Type 'x' to exit.")    

        while True:
            listing_id = input("Enter ID: ")
            if listing_id.lower() == 'x':
                conn.close()
                return
            
            if listing_id.isdigit():
                listing_id = int(listing_id)

                cursor.execute("SELECT * FROM listings WHERE id = %s AND user_id = (SELECT id FROM users WHERE username = %s)", (listing_id, self.username))
                if cursor.fetchone():
                    break
                else:
                    print("ID not found. Please try again.")
            else:
                print("Invalid input. Enter a numeric ID or 'x' to exit.")    

        # Confirm deletion
        while True:
            confirm = input("Do you want to delete this listing? Enter '1' for Yes or '2' for No: ").strip()
            if confirm == "1":
                # Delete the listing from the database
                cursor.execute("DELETE FROM listings WHERE id = %s", (listing_id,))
                conn.commit()
                print(f"Listing ID {listing_id} removed successfully!")
                break
            elif confirm == "2":
                print("No listing was deleted.")
                break
            else:
                print("Invalid choice. Please enter '1' or '2'.")

        conn.close()



    def view_own_listings(self):
        print(f"\n{self.username.upper()}'S LISTINGS - Items for Trade")
        print("----------------------------------------------------")
        conn = setup_database()
        cursor = conn.cursor()

        # Query listings specific to the current user
        cursor.execute("""
            SELECT l.item, l.description, l.quantity, l.location, l.desired_barter
            FROM listings l
            INNER JOIN users u ON l.user_id = u.id
            WHERE u.username = %s
        """, (self.username,))
        listings = cursor.fetchall()

        if listings:
            for idx, (item, description, quantity, location, desired_barter) in enumerate(listings, start=1):
                print(f"{idx}. Item: {item}")
                print(f"   Description: {description}")
                print(f"   Quantity: {quantity}")
                print(f"   Location: {location}")
                print(f"   Desired Barter Item: {desired_barter}")
                print("----------------------------------------------------")
        else:
            print("No items available for trade at the moment.")
            print("----------------------------------------------------")
        
        
        while True:
            print("\n1) EDIT LISTING\n2) REMOVE LISTING\n3) EXIT")
            
            choice = input("\nPlease enter your choice: ")
            if choice == "1":
                self.edit_listing()
            elif choice == "2":
                self.remove_listing()
            elif choice == "3":
                clear_terminal()
                return "RETURN_TO_MENU"
            else:
                print("Enter the correct number of your choice.")



    def update_listing(self):
        """
        Allows users to view and manage their barter listings, including approving or rejecting trade proposals.
        """
        conn = setup_database()
        cursor = conn.cursor()

        # Fetch user ID based on the username
        cursor.execute("SELECT id FROM users WHERE username = %s", (self.username,))
        user = cursor.fetchone()

        if user is None:
            print("User not found in the database.")
            conn.close()
            return

        user_id = user[0]

        # Fetch listings owned by the current user using their user_id
        cursor.execute("""
            SELECT l.id, l.item
            FROM listings l
            WHERE l.user_id = %s
        """, (user_id,))
        user_listings = cursor.fetchall()

        print("\nL I S T I N G  U P D A T E")
        print("----------------------------------------------")

        if not user_listings:
            print("No listings available for this user.")
            print("----------------------------------------------")
            conn.close()
            input("Press enter to exit.")
            clear_terminal()
            return


        # Iterate over listings and display
        for listing in user_listings:
            listing_id, item_name = listing
            print(f"ID {listing_id} | Item name: {item_name}")

            # Retrieve proposals for this listing
            cursor.execute("""
                SELECT id, item, description, quantity, from_user
                FROM proposals
                WHERE listing_id = %s AND status = 'Pending'
            """, (listing_id,))
            proposals = cursor.fetchall()

            if not proposals:
                print("Proposal: None")
            else:
                for proposal in proposals:
                    proposal_id, proposal_item, description, proposal_quantity, from_user = proposal
                    print(f"\nProposal ID: {proposal_id}")
                    print(f"Item Name: {proposal_item}")
                    print(f"Description: {description}")
                    print(f"Quantity: {proposal_quantity}")
                    print(f"From User: {from_user}")

                    # Ask the user whether they want to accept or reject the proposal
                    while True:
                        decision = input(f"Do you want to accept this proposal? \nEnter '1' for Yes, '2' for No, or 'x' to skip: ").strip()


                        get_username = list(User.get_logged_in_user())
                        username = get_username[1]
                        if decision == '1':
                            cursor.execute("""
                                UPDATE proposals
                                SET status = 'Accepted'
                                WHERE id = %s
                            """, (proposal_id,))
                            conn.commit()
                            print(f"Proposal ID {proposal_id} has been accepted.")
                            accept_trade(proposal_id, username)
                            break
                        elif decision == '2':
                            cursor.execute("""
                                UPDATE proposals
                                SET status = 'Rejected'
                                WHERE id = %s
                            """, (proposal_id,))
                            conn.commit()
                            print(f"Proposal ID {proposal_id} has been rejected.")
                            break
                        elif decision.lower() == 'x':
                            break
                        else:
                            print("Invalid choice. Please enter '1' to accept, '2' to reject, or 'x' to skip.")

            print("----------------------------------------------")

        conn.close()
        
        choice = input("Press enter to exit.")
        clear_terminal()