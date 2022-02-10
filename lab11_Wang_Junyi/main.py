# Junyi Wang, carsonw@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Assignment 4
# Description:
# After user input the numbers, this program calculates the largest, smallest, and average of this set of numbers.

# Create a while loop that ends when the user enters a sentinel value of -1
another = "y"

# Outer while loop for entering another set of numbers
while another == "y" or another == "Y":
    # Display the following to the user:
    print("Input an integer greater than or equal to 0 or -1 to quit:")

# initialize
    count = 0
    number = 0
    small = large = total = int(input("> "))  # first input

# Inner while loop for entering numbers
    while number != -1:
        number = int(input("> "))
        if number != -1:
            # largest number
            if number > large:
                large = number
                print(large)
            # smallest number
            if number < small:
                small = number

        total += number
        count += 1  # the number of how many number has entered
    average = (total + 1) / count  # calculate the average

# print out the largest, smallest, average number to user
    print("The largest number is", large)
    print("The smallest number is", small)
    print("The average number is", average)
    # print a new line
    print()

# ask user if they want enter another set of numbers
    another = input("Do you want to enter another set (y or n)? ")

# print a new line
print()

# if user answer they don't want to do another set, then print "goodbye"
print("Goodbye!")
