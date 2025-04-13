import sqlite3
from models.barterboardDB import *

def save_proposal(listing_id, username, item, description, quantity, from_user):
    conn = setup_database()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO proposals (listing_id, username, item, description, quantity, from_user, status)
        VALUES (%s, %s, %s, %s, %s, %s, 'Pending')
    """, (listing_id, username, item, description, quantity, from_user))
    conn.commit()
    conn.close()

