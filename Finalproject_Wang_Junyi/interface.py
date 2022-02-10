# Junyi Wang, carsonw@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Final Project
# tasks.py
# Description:
# This is the program that allow user to find out the national parks in the United States; User can view, search, and
# find the oldest and largest park.

# import tasks
import tasks

# Create the getMenuDict() function.
# • Parameters: None
# • Return value: a dictionary where the keys are letters for the
# user to input and the values are descriptions of the menu options.
def getMenuDict():
    # create menu
    # keys and corresponding values
    menuDict = {"A": "All national parks",
                "B": "Parks in a particular state",
                "C": "The largest park",
                "D": "Search for a park",
                "E": "The Oldest Park",
                "Q": "Quit"}
    # return value
    return menuDict

# Create the displayMenu() function.
# • Parameter: menuDict is a dictionary for the menu
# • Return value: None
def displayMenu(menuDict):
    # for loop to access key in menu
    for key in menuDict:
        # • Print the menu to the user using the menuDict parameter.
            print(key, "->", menuDict[key])

# Create the getUserInput() function.
# • Parameter: menuDict is a dictionary for the menu
# • Return value: a string that is a valid choice entered by the user
def getUserInput(menuDict):
    # get user's choice
    # Allow the user to enter in upper or lower case.
    user = input("Choice: ").upper()
    # while loop to check if the user's input is in the menu choice
    # The keys in the menuDict parameter have the valid letters.
    while user not in menuDict:
        # if not ask user to re-enter
        user = input("Choice: ").upper()
    # return value
    return user

# Create the printAllParks() function.
# • Parameter: parksList is a list of the parks where each park is a dictionary
# • Return value: None
def printAllParks(parkList):
    # Loop through the list and print some information for each park
    for park in parkList:
        # park name + code
        print(park["Name"], "(" + park["Code"] + ")")
        # park state location
        print("\tLocation:", park["State"])
        # park's area
        print("\tArea:", park["Acres"], "acres")
        # Date Established
        # call tasks.getDate() function to access date
        print("\tDate Established:", tasks.getDate(dateStr=park["Date"]))
        print()

# reate the getState() function.
# • Parameters: None
# • Return value: a string with a two-letter abbreviation of a state
def getState():
    # initialize - check if user entered valid value
    check = True
    # Get input from the user for a state. Allow the user to enter upper or lower case
    state = input("Enter a state: ").upper()
    # while loop to continue to ask the user for input until they enter
    # a string that only has two characters
    while check is True:
        # if not ask user to re-enter
        if len(state) != 2:
            print("Need the two letter abbreviation")
            state = input("Enter a state: ").upper()
        # else return value
        else:
            return state

# Define the printParksInState() function.
# Parameter: parksList is a list containing parks which are each represented with a dictionary object
# Return value: None
def printParksInState(parkList):
    # all the getState() function to get a state.
    userState = getState()
    # counter value to test if there is a park in the state user entered
    counter = 0
    # for loop to access key in park list
    for park in parkList:
        # if user entered value is in list
        if userState in park["State"]:
            # print following:
            # Name (Code)
            #   Location: State
            #   Area: Acres acres
            #   Date Established: Month Day, Year
            print(park["Name"], "(" + park["Code"] + ")")
            print("\tLocation:", park["State"])
            print("\tArea:", park["Acres"], "acres")
            print("\tDate Established:", tasks.getDate(dateStr=park["Date"]))
            print()
            # then add the counter
            counter += 1
    # if counter == 0, it means the state user entered has no national park
    if counter == 0:
        # print the following message to user
        print("There are no national parks in", userState, "or it is not a valid state.")
        print()

# Define the printLargestPark() function.
# • Parameter: parksList is a list containing parks which are each represented
# with a dictionary object
# • Return value: None
def printLargestPark(parkList):
    # to access the key in park list
    for park in parkList:
        # Call the tasks.getLargestPark() function to get the code of the largest park.
        parkCode = tasks.getLargestPark(parkList)
        # according to the code of the largest park, print the following info
        if parkCode in park["Code"]:
            # Name (Code)
            #   Location: State
            #   Area: Acres acres
            #   Date Established: Month Day, Year
            #   Description: Description
            print(park["Name"], "(" + park["Code"] + ")")
            print("\tLocation:", park["State"])
            print("\tArea:", park["Acres"], "acres")
            print("\tDate Established:", tasks.getDate(dateStr=park["Date"]))
            print("\tDescription:", park["Description"])
            print()

# Define the printParksForSearch() function.
# • Parameter: parksList is a list containing parks which are each represented with a dictionary object
# • Return value: None
def printParksForSearch(parkList):
    # get user's input
    print()
    user = input("Enter text for searching: ").lower()
    # counter value to test
    counter = 0
    # for loop to access key in park list
    for park in parkList:
        # check to see if the search text is in the park’s Code, Name, or Description.
        if user in park["Description"].lower() or user in park["Name"].lower() or user in park["Code"].lower():
            # if contains user's input value, the print the following:
            # Name (Code)
            #      Location: State
            #      Area: Acres acres
            #      Date Established: Month Day, Year
            #      Description: Description
            print(park["Name"], "(" + park["Code"] + ")")
            print("\tLocation:", park["State"])
            print("\tArea:", park["Acres"], "acres")
            print("\tDate Established:", tasks.getDate(dateStr=park["Date"]))
            print("\tDescription:", park["Description"])
            print()
            # add counter
            counter += 1

    # if there are no parks in the state,
    # then print a message stating that there are no national parks for the search text.
    if counter == 0:
        print("There are no national parks for the search term of", "'" + user + "'" + ".")
        print()

# Extra Credit:
# Define the printOldestPark() function.
# • Parameter: parksList is a list containing parks which are each represented with a dictionary object
# • Return value: None
def printOldestPark(parkList):
    # for loop to access key in park list
    for park in parkList:
        # Call the tasks.getOldestPark() function to get the code of the oldest park.
        parkCode = tasks.getOldestPark(parkList)
        # access the park code and print out the info about the oldest park
        if parkCode in park["Code"]:
            # Name (Code)
            #      Location: State
            #      Area: Acres acres
            #      Date Established: Month Day, Year
            #      Description: Description
            print(park["Name"], "(" + park["Code"] + ")")
            print("\tLocation:", park["State"])
            print("\tArea:", park["Acres"], "acres")
            print("\tDate Established:", tasks.getDate(dateStr=park["Date"]))
            print("\tDescription:", park["Description"])
            print()
