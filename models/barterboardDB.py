import mysql.connector
from mysql.connector import errorcode, errors

# Database setup

def setup_database():
    try:
        conn = mysql.connector.connect(user='root', password='Kahitano1', host='localhost', database='BarterBoard')
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name")
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)