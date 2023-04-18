import datetime
import json
from Functions import *
from Config import *
import os
import time

# Function which handles the main menu screen prompt
def mainMenu():
    print("Main Menu")
    while True:
        print('\nMenu Options:')
        # Create the option menu
        print('1 - Enter Job Data For Today')
        print('2 - Update Job Data For a Date')
        print('3 - Generate Timesheet')
        print('4 - Generate Safety Log')
        print('5 - Help Page')
        print('6 - Exit the program')
        # Asks the user for their input')
        MenuSelect = input('\nPlease select a menu option: ')
        # Menu option 1 will enter new data, uses functions from user input program
        if MenuSelect == '1':
            CheckDataDirectory()
        elif MenuSelect == '2':
            print("Program exiting...")
            time.sleep(2)
            exit()
        elif MenuSelect == '3':
            print("Program exiting...")
            time.sleep(2)
            exit()
        elif MenuSelect == '4':
            print("Program exiting...")
            time.sleep(2)
            exit()
        elif MenuSelect == '5':
            print("Program exiting...")
            time.sleep(2)
            exit()
        elif MenuSelect == '6':
            print("Program exiting...")
            time.sleep(2)
            exit()
        else:
            print('That is not a valid option')

mainMenu()
