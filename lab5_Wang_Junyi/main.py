# Junyi Wang, carsonw@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Lab 5

# import random module
import random

# create lists
nouns = ["dog", "dragon", "caterpillar"]
verbs = ["ran", "slept", "ate", "swan"]
articles = ["a", "an", "the"]

# while loop
user_num = 0
while user_num != 5:
    # print menu
    print("Welcome to the Sentence Generator")
    print("1. View Words")
    print("2. Add Noun")
    print("3. Remove Verb")
    print("4. Generate Sentence")
    print("5. Exit")

    # get user's input
    user_num = int(input("> "))

    # branching
    if user_num == 1:
        # print list
        print("articles:", articles)
        print("nouns:", nouns)
        print("verbs:", verbs)
    elif user_num == 2:
        # add noun
        new_noun = input("Enter the word: ")
        nouns.append(new_noun)
        print("nouns:", nouns)
    elif user_num == 3:
        # remove verb
        bad_verb = input("Enter the word: ")
        if bad_verb in verbs:
            verbs.remove(bad_verb)
            print("verbs:", verbs)
        else:
            print("Invalid word")
    elif user_num == 4:
        # generate sentence
        # article noun verb article noun
        articles1 = random.choice(articles)
        noun1 = random.choice(nouns)
        random_verb = random.choice(verbs)
        articles2 = random.choice(articles)
        noun2 = random.choice(nouns)
        print(articles1, noun1, random_verb, articles2, noun2)
    elif user_num == 5:
        print("Thank you for using the Sentence Generator!")
    else:
        print("Invalid choice")
    print()
