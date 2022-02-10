# Junyi Wang, carsonw@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Final Project
# tasks.py
# Description:
# This is the program that allow user to find out the national parks in the United States; User can view, search, and
# find the oldest and largest park.

# import tasks, interface
import tasks
import interface

# define main()
def main():
    # Print the following message to the user:
    print("National Parks")
    print()
    # access park list by calling the createListOfParks() from tasks.py
    parkList = tasks.createListOfParks(fileName="national_parks.csv")
    # access the menu by calling getMenuDict() from interface.py
    menuDic = interface.getMenuDict()

    # Use a while loop to display the menu, get the user’s choice, and respond to the user’s
    # choice while the user does not enter "Q" or "q".
    while True:
        # display the menu to user
        interface.displayMenu(menuDic)
        # get user's input choice
        user = interface.getUserInput(menuDic)
        # Use branching to call the appropriate function in the interface file depending on the user’s input.
        if user == "A":
            interface.printAllParks(parkList)

        elif user == "B":
            interface.printParksInState(parkList)

        elif user == "C":
            interface.printLargestPark(parkList)

        elif user == "D":
            interface.printParksForSearch(parkList)

        elif user == "E":
            interface.printOldestPark(parkList)

        # if user enter Q, quit the program
        elif user == "Q":
            # return False
            return False

# call main()
main()
