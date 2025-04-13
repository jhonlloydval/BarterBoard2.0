import os

# Clear the terminal OMG MARUNONG NA Q
def clear_terminal():

    # To check for OS
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')

