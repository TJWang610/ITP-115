# Junyi Wang, carsonw@usc.edu
# ITP 115, Fall 2021
# Section: bagel
# Assignment 10
# Description:
# Create a dictionary to manage data. This is a program that manages a user’s music library.
# Allow the user to insert, update, and delete data from the dictionary.
# Also, for bonus, allow user to customize their own music library

# import MusicLibraryHelper
import MusicLibraryHelper

# import random
import random

# def displayMenu()
# o Parameter: None
# o Return value: None
def displayMenu():
    # o Print out the menu options to the user:
    print("Manage Your Music Library"
          "\n a) Display library"
          "\n b) Display artists"
          "\n c) Add an artist/album"
          "\n d) Delete an album"
          "\n e) Delete an artist"
          "\n f) Generate a random playlist"
          "\n g) Generate your custom playlist"
          "\n h) Exit")

# define displayLibrary(musicLibrary)
# o Parameter: a dictionary representing the music library
# o Return value: None
def displayLibrary(musicLibrary):
    # o Print out the entire music library
    for key in musicLibrary:
        print("Artist:", key, "\n   Albums:")
        for keys in musicLibrary[key]:
            print("     ", keys)

# Define the displayArtists(dictionary) function.
# o Parameter: a dictionary representing the music library o Return value: None
def displayArtists(musicLibrary):
    print("Artists: ")
    # o Print out the artists in the music library.
    for artists in musicLibrary:
        print("  ", artists)

# Define the addAlbum(dictionary) function.
# o Parameter: a dictionary representing the music library o Return value: None
def addAlbum(musicLibrary):
    # Get input from the user for the name of the artist and the name of the album that they want to add
    # Use the str.title() method to convert both of them to Title Case
    addArtist =str.title(input("Enter artist: ").lower())
    addAlbum =str.title(input("Enter album: ").lower())

    # Check if the artist is already in the dictionary.
    # If the artist is not in the dictionary,
    # add a new key (artist) to the dictionary along with the new value (list containing the new album).
    if addArtist not in musicLibrary.keys():
        musicLibrary[addArtist] = [addAlbum]
    # if yes add the album to the artist’s existing list of albums
    # If the album already exists, then do not add it.
    else:
        if addAlbum not in musicLibrary[addArtist]:
            musicLibrary[addArtist].append(addAlbum)

# Define the deleteAlbum(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: a boolean value
# True if an album was successfully deleted, or False if the album was not successfully deleted
# o Get input from the user for the name of the artist and the name of the album that they want to delete.
def deleteAlbum(musicLibrary):
    artist = str.title(input("Enter artist: ").lower())
    album = str.title(input("Enter album: ").lower())
    if artist in musicLibrary:
        # If the album is not in the dictionary, do not modify the dictionary and return False.
        if album not in musicLibrary[artist]:
            return False

        # remove album
        else:
            musicLibrary[artist].remove(album)
            if not musicLibrary[artist]:
                del musicLibrary[artist]
            return True

    # If the artist is not in the dictionary, do not modify the dictionary and return False.
    else:
        return False

# Define the deleteArtist(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: a boolean value - True if an artist was successfully deleted,
# or False if the artist was not successfully deleted
# o Get input from the user for the name of the artist and the name of the album that they want to delete.
def deleteArtist(musicLibrary):
    artist = str.title(input("Enter artist to delete: ").lower())
    # If the artist is not in the dictionary, do not modify the dictionary and return False.
    if artist not in musicLibrary:
        return False
    # if yes, then delete the artist
    else:
        del musicLibrary[artist]
        return True

# Define the generateRandomPlaylist(dictionary) function.
# o Parameter: a dictionary representing the music library
# o Return value: None
def generateRandomPlaylist(musicLibrary):
    print("Here is your random playlist:")
    # Generate a random playlist for the user by randomly selecting one album from every artist in the library.
    for key in musicLibrary:
        print("  " + random.choice(musicLibrary[key]), "by", key)

# Bonus Question:
# Define generateCustomPlaylist(dictionary) function
# § Input: the dictionary representing the music library
# § Return value: none
# § Generate a custom playlist by letting the user select the artists and their albums.
def generateCustomPlaylist(musicLibrary):
    # create a control value in order to check if user want to continue later/ for loop
    controlValue = "y"
    # create a empty list for user to customize
    playlist = []

    # loop
    while controlValue == "y":
        # Print the current playlist (at first it should be empty)
        print()
        print("Following is your current playlist: ")
        for list in playlist:
            print(" ", list)
        print()

        # Print the artists in the library and a number next to each artist's name
        print("Following are the artists in the library:")

        # Hint: store a list of the artists to make the next step easier.
        numbersArtist = 0
        numbersAlbum = 0
        artist = []
        album = []
        uerArtOption = []
        userAlbOption = []

        # Ask the user to select an artist by selecting their corresponding number
        for key in musicLibrary.keys():
            # print out the artists' name and their attribute number
            print(str(numbersArtist) + ".", key)
            artist.append(key)
            uerArtOption.append(numbersArtist)
            numbersArtist += 1

        # ask user to enter the choice number to add the artist into their list
        choice = int(input("Please select an artist by entering their corresponding number: "))
        # error checking
        while choice not in uerArtOption:
            print("Invalid Choice")
            choice = int(input("Please select an artist by entering their corresponding number: "))
        userArtChoice = artist[choice]

        print()
        # Using the selected artist, print out a list of the artist's albums with a number next to each album name.
        print("Following are the albums of", str(userArtChoice), "in the library:")
        # Ask the user to select an album by selecting their corresponding number
        for a in musicLibrary[userArtChoice]:
            print(str(numbersAlbum) + ".", a)
            album.append(a)
            userAlbOption.append(numbersAlbum)
            numbersAlbum += 1

        # ask user to enter the choice number to add the album into their list
        choice2 = int(input("Please select an album by entering their corresponding number: "))
        # error checking
        while choice2 not in userAlbOption:
            print("Invalid Choice")
            choice2 = int(input("Please select an artist by entering their corresponding number: "))
        userAlbChoice = album[choice2]

        # if user want to add another list later, use append to add them
        playlist.append(userAlbChoice + " by " + userArtChoice)

        # ask user if they want to continue adding to their playlist. Be sure to include error checking
        controlValue = input("Do you want to continue adding to their playlist?(y/n) ").lower()
        # error checking
        while controlValue not in ["y", "n"]:
            print("Invalid Choice")
            controlValue = input("Do you want to continue adding to their playlist?(y/n) ").lower()

    # Once the user is done building their playlist, print it out one final time
    print("This is your final playlist:")
    for list in playlist:
        print("  ", list)

# Define and call the main() function.
# o Create a variable to hold the file name and initialize it to "musicLibrary.dat".
# o Create a dictionary by calling the MusicLibraryHelper.loadLibrary() function which returns a dictionary.
# Capture the return value in a variable, which you will using throughout the main() function.
def main():
    musicLibrary = MusicLibraryHelper.loadLibrary("musicLibrary.dat")
    allChoice = ["a", "b", "c", "d", "e", "f", "g", "h"]
    # Using a while loop, display the menu to the user by calling the displayMenu() function
    while True:
        # display the menu to the user by calling the displayMenu()
        displayMenu()
        # get user input using "Choice: "
        choice = input("Choice: ").lower()
        while choice not in allChoice:
            print("Invalid entry")
            print()
            displayMenu()
            choice = input("Choice: ").lower()

        # Based on the user’s input, call the corresponding function. Allow the user to
        # enter their choice in upper or lower case.
        if choice == "a":
            displayLibrary(musicLibrary)

        elif choice == "b":
            displayArtists(musicLibrary)

        elif choice == "c":
            addAlbum(musicLibrary)

        # The deleteAlbum() and deleteArtist() functions have return values. Based on the return value (boolean),
        # print out an appropriate message about whether or not the delete was successful.
        elif choice == "d":
            delete = deleteAlbum(musicLibrary)
            if delete:
                print("Delete album success")
            else:
                print("Delete album failed")

        elif choice == "e":
            delete = deleteArtist(musicLibrary)
            if delete:
                print("Delete artist success")
            else:
                print("Delete artist failed")

        elif choice == "f":
            generateRandomPlaylist(musicLibrary)

        # Bonus Question
        elif choice == "g":
            # call the function
            generateCustomPlaylist(musicLibrary)
            print()
            # ask users if they want to save their customized music library
            choice = input("Do you want to save your customized music library?(y/n) ").lower()
            # if yes save it
            if choice == "y":
                name = input("Enter music library filename: ")
                print("Saved music library to", name)
                MusicLibraryHelper.saveLibrary(name, musicLibrary)

            print()
            # ask users if they want to try other choice in the Music Library
            choice2 = input("Do you want to try other option in 'Manage Your Music Library'?(y/n) ")
            # if users don't want to continue, return False, and end the program
            while choice2 != "y":
                print("Thank you for using the custom playlist option!")
                return False

        elif choice == "h":
            # When the user enters the appropriate choice to quit, ask the user for a file name for the music library.
            name = input("Enter music library filename: ")
            # Save the music library using the MusicLibraryHelper.saveLibrary() function and
            # print out a message to the user.
            print("Saved music library to", name)
            print()
            MusicLibraryHelper.saveLibrary(name, musicLibrary)
            return False

        # If the enter enters an invalid choice, print the following message:
        else:
            print("Invalid entry")
        print()
main()
