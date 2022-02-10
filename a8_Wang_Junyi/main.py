# Junyi Wang, carsonw@usc.edu
# Fall 2021, ITP 115
# section: Bagel
# Assignment 8
# Description:
# This program allow user to play Tic Tac Toe with either computer or other user.
# The program will let the two players to place a "x" or a "o" on the board to indicate when someone wins
# or when a stalemate occurs. Define and call functions to simulate a game of Tic Tac Toe.


import TicTacToeHelper

# extra credit: for computer to choose
import random

# extra credit: def printPrettyBoard function
def printPrettyBoard(boardList):
    # print a new line
    print()
    counter = 0
    for a in range(2):
        for b in range(2):
            print(boardList[counter], end=" | ")
            counter += 1
        print(boardList[counter])
        counter += 1
        print("---------")
    for c in range(2):
        print(boardList[counter], end=" | ")
        counter += 1
    print(boardList[counter])
    counter += 1
    print()

# define isValidMove function, to check if enter move is valid
# o Parameter 1: a list representing the board
# o Parameter 2: an integer corresponding to the index position that a user would like to place their letter on
# o Return value: a boolean value (True or False)
def isValidMove(boardList, spot):
    if spot not in boardList:
        return False
    elif int(spot) > 8 or int(spot) < 0:
        return False
    elif boardList[int(spot)] == "x" or boardList[int(spot)] == "o":
        return False
    return True

# Define the updateBoard(boardList, spot, playerLetter) function.
# updates the board with the correct move
def updateBoard(boardList, spot, playerLetter):
    # replace the its original spot with the player letter
    spot = int(spot)
    boardList[spot] = playerLetter


# Define the playGame() function.
# o Parameter: None
# o Return value: None
def playGame():
    # create boardList: list for the board
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # extra credit: users' choice list
    players = ["x", "o"]

    # initiative
    # Create an int variable to keep track of the total number of moves that have been made.
    count = 1
    turn = 0
    # Create a string variable that will be used to see if there is a winner
    winner = "n"

    # extra credit: give the user the option of starting the game as either player x or player o.
    # plus the error checking if user entered validly
    start = input("Which user would like to start first? (x/o): ")
    while start not in players:
        start = input("Which user would like to start first? (x/o): ")
    if start == "x":
        turn = 0
    elif start == "o":
        turn = 1

    # as the game start print the following to user
    # print the initial pretty board to user
    printPrettyBoard(boardList)

    # while loop
    while winner == "n":
        print(turn % 2)
        # Depending on the who’s turn it is, ask the user what position they would like to put their letter on the board
        move = input("Player " + players[turn % 2] + " pick a spot: ")

        # loop: only if the user has inputted an invalid spot
        # calling the isValidMove() function
        while not isValidMove(boardList, move):
            move = input("Player " + players[turn % 2] + " pick a spot: ")

        # update the board with the move by calling the updateBoard() function if the move is valid
        updateBoard(boardList, move, players[turn % 2])

        # to determine if the game is over
        winner = TicTacToeHelper.checkForWinner(boardList, count)

        # prints the board to user for each round
        printPrettyBoard(boardList)

        # count vaules
        count += 1
        turn += 1

    # print the game result to user
    print("Game Over!")
    if winner in ["x", "o"]:
        print("Player", winner, "is the winner!")
    else:
        print("Stalemate reached!")

# extra credit: def playComputer function, this function is for when user decide to play with computer
def playComputer():
    # print the following information to user
    print("You are playing against the computer in this game.")
    print("Reminder: Computer will be the player x, and you will be the player o.")

    # extra credit: users' choice list
    players = ["x", "o"]

    # create boardList: list for the board
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # initiative
    # Create an int variable to keep track of the total number of moves that have been made.
    count = 1
    turn = 0
    winner = "n"

    # extra credit: ask player to choose if they want to let computer start or they want to start first + error checking
    print("Type x if you would like computer to start first; type o if you would like to start first.")
    start = input("Who would you like to start first? (x/o): ")
    while start not in players:
        start = input("Who would you like to start first? (x/o): ")
    if start == "x":
        turn = 0
    elif start == "o":
        turn = 1

    # print the initial pretty board to user
    printPrettyBoard(boardList)

    # while loop
    while winner == "n":

        # computer choice - randomly chosen
        if players[turn % 2] == "x":
            move = str(random.randint(0, 8))
            # loop: to check if computer's choice is an invalid spot
            while not isValidMove(boardList, move):
                move = str(random.randint(0, 8))
            print("The computer chose spot", move + ".")

        # get player input for spot
        else:
            move = input("Please pick a spot: ")
            # loop: to check if user's input is an invalid spot
            while not isValidMove(boardList, move):
                move = input("Please pick a spot: ")

        # update the board with the move by calling the updateBoard() function if the move is valid
        updateBoard(boardList, move, players[turn % 2])

        # to determine if the game is over
        winner = TicTacToeHelper.checkForWinner(boardList, count)

        # print the pretty board to user for each round
        printPrettyBoard(boardList)

        # count values
        count += 1
        turn += 1

    # print the game result to user: whether computer wins or the user
    print("Game Over!")
    if winner in ["x", "o"]:
        if winner == "x":
            print("Computer wins.")
        else:
            print("Congratulations! You win!")
    else:
        print("Stalemate reached!")

# define the main() function
# Define and call the main() function.
# o Parameter: None
# o Return value: None
def main():
    # Print the message: "Welcome to Tic Tac Toe!".
    print("Welcome to Tic Tac Toe!")

    play = "y"
    # Use a while loop to allow the user to keep playing a new game of Tic Tac Toe if they enter "y" or "Y".
    while play == "y":
        # ask user play with computer or other user
        print("Type c if you want to play with computer; type p if you want to play with another user!")
        player = input("Who would like to play with? (c/p): ").lower()
        while player not in ["c", "p"]:
            player = input("Single player or multiplayer? (c/p): ").lower()
        if player == "c":
            print()
            # Call the playComputer() function if user choose play a round of Tic Tac Toe with computer
            playComputer()
        else:
            print()
            # Call the playGame() function if user choose play a round of Tic Tac Toe with another user
            playGame()
        # ask user if they want to play again
        play = input("Would you like to continue (y/n): ").lower()
        print()
    print("Goodbye!")

main()