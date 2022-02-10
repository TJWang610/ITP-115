# Junyi Wang, carsonw@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Final Project
# tasks.py
# Description:
# This is the program that allow user to find out the national parks in the United States; User can view, search, and
# find the oldest and largest park.

# Define the createListOfParks() function
# Parameter: fileName is the name of the CSV file to read and it has a default
# value of "national_parks.csv"
# Return value: a list of dictionary objects where the
# keys are the strings from the header row and the values are the information from the rest of the CSV file
def createListOfParks(fileName="national_parks.cvs"):
    # create open parkList
    parkList = []
    # open the file
    file = open(fileName, "r")
    # get the header row and put it into a list
    header = file.readline()
    header = header.strip()
    keys = header.split(",")
    # use for description; in order to get the full description
    # before description
    keys1 = keys[:7]
    # full description
    keys2 = keys[7:]

    # create for loop
    for line in file:
        # create line in file into list
        line1 = line.strip()
        parks = line1.split(",")
        # for description （str.join()）
        parks1 = ",".join(parks[7:]).strip('"')
        # create a dictionary
        parkDict = {}
        # for loop (before description)
        for key in keys1:
            # loop through key to add info to dict
            parkDict[key] = parks[keys1.index(key)]
        # for loop (description only)
        for key1 in keys2:
            # loop through key to add info to dict
            parkDict[key1] = parks1
        # append to the parkList
        parkList.append(parkDict)
    # return Value
    return parkList

# Define the getDate() function.
# • Parameter: dataStr is a string containing the date (YYYY-MM-DD)
# • Return value: a string with the date in the following format: Month Day, Year
def getDate(dateStr):
    # create list of month names
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    # create list
    date = dateStr.split("-")
    # access moth
    month = int(date[1])
    # get the month name from the month name list created
    month2 = months[month-1]
    # access year
    year = date[0]
    # access day
    day = date[2]
    # date in the following format: Month Day, Year
    # using "%02d" to create 00 format number
    dateFinal = month2 + " " + day + ", " + year
    # return value
    return dateFinal

# Define the getLargestPark() function.
# • Parameter: parksList is a list of the parks where each park is a dictionary
# • Return value: a string that is the park code of the park with the largest area
def getLargestPark(parkList):
    # initialize
    large = 0
    # create an empty list for access parkCode
    parkCode = " "
    # for loop to access key in parkList
    for park in parkList:
        # largest number among parks' acres
        if int((park["Acres"])) > large:
            large = int(park["Acres"])
            # get the park code
            parkCode = park["Code"]
    # return value
    return parkCode

# Extra Credit:
# Define the getOldestPark() function.
# • Parameter: parksList is a list of the parks where each park is a dictionary
# • Return value: a string that is the park code of the park with the oldest year
def getOldestPark(parkList):
    # initialize
    older = 9999
    # create an empty list for access parkCode
    parkCode = " "
    # for loop to access key in parkList
    for park in parkList:
        # access the date in park list
        date = park["Date"].split("-")
        # get the year
        year = date[0]
        # oldest year among parks
        if int(year) < older:
            older = int(year)
            # get the parkCode
            parkCode = park["Code"]
    # return value
    return parkCode





