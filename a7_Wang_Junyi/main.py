import TicTacToeHelper

# extra credit: for computer to choose
import random

# extra credit: def printPrettyBoard function
def printPrettyBoard(boardList):
    # print a new line
    print()
    counter = 0
    for a in range(3):
        for b in range(3):
            if b != 2:
                print(boardList[counter], end=" | ")
            else:
                print(boardList[counter])
            counter += 1
        print("---------", end="")
        print()

# define isValidMove function, to check if enter move is valid
# o Parameter 1: a list representing the board
# o Parameter 2: an integer corresponding to the index position that a user would like to place their letter on
# o Return value: a boolean value (True or False)
def is_valid_move(board_list, spot):
    if spot < 0 or spot > 8:
        return False # returns false if you enter an invalid integer
    elif board_list[spot] == "x" or board_list[spot] =="o":
        return False
    else:
        return True

# Define the updateBoard(boardList, spot, playerLetter) function.
# updates the board with the correct move
def updateBoard(boardList, spot, playerLetter):
    # replace the its original spot with the player letter
    boardList[spot] = playerLetter


# Define the playGame() function.
# o Parameter: None
# o Return value: None
def playGame():
    # extra credit: users' choice list
    players = ["x", "o"]
    # create boardList: list for the board
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # counter for the turn and for game ending logic
    count = 1
    turn = 0
    winner = "n"

    # extra credit: give the user the option of starting the game as either player x or player o.
    # plus the error checking if user entered validly
    start = input("Which user would like to start first? (x/o): ")
    while start not in players:
        start = input("Which user would like to start first? (x/o): ")
    if start == "x":
        turn = 0
    else:
        turn = 1
    print("\nWelcome to Tic Tac Toe!!")
    printPrettyBoard(boardList)

    # while loop for the duration of one game
    while winner == "n":
        # get input for spot
        move = input("Player " + players[turn % 2] + " pick a spot: ")
        # loop question if input is invalid spot on board
        while not isValidMove(boardList, move):
            move = input("Player " + players[turn % 2] + " pick a spot: ")
        # updates the board
        updateBoard(boardList, move, players[turn % 2])
        # sets gameStatus equal to function to see result of each round
        winner = TicTacToeHelper.checkForWinner(boardList, count)
        # prints the board after each round
        printPrettyBoard(boardList)
        # adds one to count
        count += 1
        turn += 1
    # prints game result based on game result lol
    print("And that's the game!!!")
    if winner in ["x", "o"]:
        print("Player " + winner + " wins!!!")
    else:
        print("Tough luck. That's a stalemate!")

# def playComputer function, this function is for when user decide to play with computer
def playComputer():
    print("You are now playing against the computer.")
    print("The computer will play as player x.")
    # list for the players
    players = ["x", "o"]
    # list for the board
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    # counter for the turn and for game ending logic
    count = 1
    turn = 0
    winner = "n"
    # extra work for allowing player to choose who starts with error checking
    start = input("Who would you like to start? Remember that you are player o. (x/o): ")
    while start not in players:
        start = input("Who would you like to start? Remember that you are player o. (x/o): ")
    if start == "x":
        turn = 0
    else:
        turn = 1

    print("Here is a fresh board!")
    printPrettyBoard(boardList)
    # while loop for the duration of one game
    while winner == "n":
        # get computer choice, have to cast to string for isValidMove function
        if players[turn%2] == "x":
            move = str(random.randint(0, 8))
            while not isValidMove(boardList, move):
                move = str(random.randint(0, 8))
            print("The computer chose spot " + move + ".")
        # get player input for spot
        else:
            move = input("Pick a spot: ")
            # loop question if input is invalid spot on board
            while not isValidMove(boardList, move):
                move = input("Pick a spot: ")
        # updates the board
        updateBoard(boardList, move, players[turn % 2])
        # sets gameStatus equal to function to see result of each round
        winner = TicTacToeHelper.checkForWinner(boardList, count)
        # prints the pretty board after each round
        printPrettyBoard(boardList)
        # adds one to count
        count += 1
        turn += 1
    # prints game result based on game result lol
    print("And that's the game!!!")
    if winner in ["x", "o"]:
        if winner == "x":
            print("Computer wins. They always do...")
        else:
            print("You win!!!")
    else:
        print("Tough luck. That's a stalemate!")

# main function to put everything together
def main():
    # variable to control the possibility of sequential games
    play = "y"
    while play == "y":
        # single or multiplayer
        player = input("Single player or multiplayer? (s/m): ").lower()
        while player not in ["s", "m"]:
            player = input("Single player or multiplayer? (s/m): ")
        if player == "s":
            playComputer()
        else:
            playGame()
        play = input("Would you like to continue (y/n): ")
        # additional error checking
        while play not in ["y", "n"]:
            play = input("Would you like to continue (y/n): ")
main()