# Junyi Wang, carsonw@usc.edu
# Fall 2021, ITP115
# Section: bagel
# lab 8

import random

# global constants (alternative way)
# FACES = ["heads", "tails"]

# define functions
# function: coin
# parameters: None
# return value: string that is either "heads" or "tails"
def coin():
    randomInt = random.randrange(0, 2)
    # branching
    if randomInt == 0:
        face = "heads"
    else:
        face = "tails"
    return face
    # ALTERNATIVE WAY:
    # return random.choice(FACES)

# function: experiment
# parameters: None
# Return value: an int that equals the number of flips
# it took to get three "heads" in a row
def experiment():
    flips = 0
    heads = 0
    # loop to get 3 heads in a row
    while heads < 3:
        coinFlip = coin()
        flips += 1
        if coinFlip == "heads":
            heads += 1
        else:  #tails
            heads = 0

    # after while loop, but inside the experiment
    return flips

#fuction: main
# parameters; None
# return value: None
# it's the staring point
# define main
def main():
    # avarage = total/num
    total = 0
    numRuns = 10
    for count in range(numRuns):
        numFlips = experiment()
        total += numFlips

    average = total / numRuns
    print("The average for 3 heads in a row is:", average)

main()
