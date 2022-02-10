# Junyi Wang, carsonw@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Assignment 7
# Description: By using functions, this game(program) allows user to play rock, paper and scissor with computer

import random

# Define the displayMenu() function
# Parameters (input): None
# Return value (output): None
# Displays the game rules to the user:
def displayMenu():
    print("Let's play Rock Paper Scissors.")
    print("The rules of the game are:")
    print("   Rock smashes Scissors")
    print("   Scissors cut Paper")
    print("   Paper covers Rock")
    print("   If both the choices are the same, it's a tie")

# Define the getComputerChoice() function.
# Parameters (input): None
# Use the random module to get a random integer between 0 and 2.
def getComputerChoice():
    computer_choice = random.randint(0, 2)
    # Return value (output): an integer that is a random number between 0 and 2.
    return computer_choice

# Define the getPlayerChoice() function.
# Parameters (input): None
def getUserChoice():
    # Display the following message to the user:
    print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")
    user_choice = int(input("> "))
    while user_choice < 0 or user_choice > 2:
        user_choice = int(input("> "))
    # Return value (output): an integer that represents the user’s choice
    return user_choice

# Define the playRound(computerChoice, playerChoice) function.
# Parameter 1: an integer representing the computer’s choice
# Parameter 2: an integer representing the player’s choice
# Return value: an integer the represents if there was a tie or the winner
def playRound(computerChoice, playerChoice):
    if playerChoice == 0 and computerChoice == 2:
        print("You Win!")
        # Return 1 if the player won the round
        return 1
    elif playerChoice == 0 and computerChoice == 1:
        print("Computer Wins!")
        # Return -1 if the computer won the round
        return -1
    elif playerChoice == 1 and computerChoice == 2:
        print("Computer Wins!")
        # Return -1 if the computer won the round
        return -1
    elif playerChoice == 1 and computerChoice == 0:
        print("You Win!")
        # Return 1 if the player won the round
        return 1
    elif playerChoice == 2 and computerChoice == 0:
        # Return -1 if the computer won the round
        print("Computer Wins!")
        return -1
    elif playerChoice == 2 and computerChoice == 1:
        print("You Win!")
        # Return 1 if the player won the round
        return 1
    else:
        print("It's a tie!")
        # Return 0 if there is a tie
        return 0

# Define the continueGame() function.
# Parameters: None
def continueGame():
    # Ask the user if they want to continue. Allow them to enter upper or lower case letters.
    play_again = input("Do you want to continue playing (y or n)? ")
    print()
    # Return True if the user enters "y" or "Y". Otherwise, return False.
    if play_again.lower() == "y":
        # Return value: a bool (Boolean), True or False
        return True
    elif play_again.lower() == "n":
        # Return value
        return False

# Define and call the main() function. no parameters nor a return value.
def main():
    pWins = 0
    cWins = 0
    tie = 0
    newGame = True

# track of the number of ties, wins by the player, and wins by the computer
# using while loop
    while newGame:
        displaymenu()
        player = getUserChoice()
        computer = getComputerChoice()
        game = playRound(computer, player)
        if game == 1:
            pWins += 1
        elif game == -1:
            cWins += 1
        elif game == 0:
            tie += 1

        # Call the continueGame() function to ask the user if they want to continue,
        # and use their response to control the while loop.
        newGame = continueGame()

    # display the final results
    print("You won", pWins, "game(s).")
    print("The computer won", cWins, "game(s).")
    print("You tied with the computer", tie, "times(s).")

main()
