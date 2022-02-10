"""
Tic Tac Toe Helper: provides two functions to be used for a game of Tic Tac Toe
1) Check for winner: determines the current state of the board
2) Print ugly board: prints out a tic tac toe board in a basic format
"""


# Given a tic, tac, toe board determine if there is a winner
# Function inputs:
#     board_list: an array of 9 strings representing the tic tac toe board
#     move_counter: an integer representing the number of moves that have been made
# Returns a string:
#     'x' if x won
#     'o' if o won
#     'n' if no one wins
#     's' if there is a stalemate
def checkForWinner(board_list, move_counter):
    j = 0
    for i in range(0, 9, 3):
        # Check for 3 in a row
        if board_list[i] == board_list[i+1] == board_list[i+2]:
            return board_list[i]

        # Check for 3 in a column
        elif board_list[j] == board_list[j+3] == board_list[j+6]:
            return board_list[j]

        # Check the diagonal from the top left to the bottom right
        elif board_list[0] == board_list[4] == board_list[8]:
            return board_list[0]

        # Check the diagonal from top right to bottom left
        elif board_list[2] == board_list[4] == board_list[6]:
            return board_list[2]
        j += 1

    # If winner was not found and board is completely filled up, return stalemate
    if move_counter > 8:
        return "s"

    # Otherwise, 3 in a row anywhere on the board
    return "n"


# Print out the tic tac toe board
# Input: list representing the tic tac toe board
# Return value: none
def printUglyBoard(board_list):
    print()
    counter = 0
    for i in range(3):
        for j in range(3):
            print(board_list[counter], end="  ")
            counter += 1
        print()
