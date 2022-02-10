# Junyi Wang, carsonw@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Assignment 9
# Description:
# This is an program named "language translator" that translates English words
# to another language using data from a CSV file

# Define the getLanguages(fileName) function.
# o Parameter: fileName is a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# o Return value: a list of strings representing the languages in the header row
def getLanguages(fileName="languages.csv"):
    # open the file
    file = open(fileName, "r")
    # get the header row with the languages and put it into a list
    header = file.readline().strip()
    languages = header.split(",")
    # close the file
    file.close()
    # return vaule
    return languages

# Define the getTranslationLanguage(langList) function.
# o Parameter: langList is a list of the languages
# o Return value: a string for the language to translate words into
def getSecondLanguage(langList):
    # print following to user
    print("Translate English words to one of the following languages:")
    print("\t", end="")
    # Removes English choice in the langList by using slicing
    for languages in langList[1:]:
        # print language list to user(without English)
        print(languages, end=" ")
        # to make a new line start with Japanese
        if languages == "Italian":
            print("\n", end="\t")

    # create list for error checking
    errorcheck = []
    for word in langList:
        word = word.lower()
        # append the word
        errorcheck.append(word)
    choice = input("\nEnter a language: ").lower().strip()
    while choice not in errorcheck:
        print("This program does not support", choice.capitalize())
        choice = input("Enter a language: ").lower().strip()
    # Return the language such that the first letter is capitalized and the remaining letters are lower case
    choice = choice.capitalize()
    return choice

# Define the readFile(langList, langStr, fileName) function.
# o Parameter 1: langList is a list of the languages
# o Parameter 2: langStr is a string of containing the name of a language and it has
# a default value of "English"
# o Parameter 3: fileName is a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# o Return value: a list of words in the language identified by the langStr parameter
def readFile(langList, langStr="English", fileName="languages.csv"):
    # create an empty list
    list = []
    # Open the CSV file and read the header row to skip it.
    fiileIn = open(fileName, "r")
    header = fiileIn.readline()
    # Use the langList and langStr parameters to determine the index of the language.
    language_index = langList.index(langStr)
    # Loop through the rest of the file. Each line of data will have an extraneous new line at the end
    for line in fiileIn:
        # remove
        line = line.strip()
        # break up the line into a list of strings
        line = line.split(",")
        translation = line[language_index]
        # Get the correct word and append it to the list.
        list.append(translation)
    # close file
    fiileIn.close()
    #return value
    return list

# Define the createResultsFile(language) function.
# o Parameter: language is a string containing the name of the language for
# translation
# o Return value: None
def createResultsFile(language):
    resultsFile = language + ".txt"
    out_file = open(resultsFile, "w")
    print("Words translated from English to", language, file=out_file)
    out_file.close()

# Define the translateWords(englishList, translationList, language) function.
# o Parameter 1: englishList is a list of words in English
# o Parameter 2: translationList is a list of words in another language (not English)
# o Parameter 3: language is a string containing the language of the words in the
# translationList
# o Return value: none
def translateWords(englishList, translationList, language):
    # open the results file
    resultsFile = open(language, "a")
    # for error checking
    choice = "y"
    # while loop to translate the language
    while choice == "y":
        translate = input("\nEnter a word to translate: ")
        if translate not in englishList:
            print(translate, "is not in the list")
            choice = input("Another word (y or n)? ").lower()
        else:
            # get translated word by index
            wordIndex = englishList.index(translate)
            tranWord = translationList[wordIndex]
            if tranWord == "-":
                print(translate, "is not in the list")
                choice = input("Another word (y or n)? ").lower()
            # translation and write it in the new file
            else:
                print(translate, "is translated to", tranWord)
                print(translate, "=", tranWord, file=resultsFile)
                choice = input("Another word (y or n)? ").lower()
        # if the word is not in the english list, tell the user
    resultsFile.close()
    print("Translated words have been saved to", language)

def main():
    # print following
    print("Language Translator")
    # Call the getLanguages() function to get the list of languages.
    headers = getLanguages("languages.csv")
    # Call the readFile() function to read the CSV file for the English words
    englishList = readFile(headers)
    # Call the getTranslationLanguage() function to get the language to use for translation
    language = getSecondLanguage(headers)
    # Call the readFile() function to read the CSV file for the translation language.
    secondList = readFile(headers, language, "languages.csv")
    # open the results file
    createResultsFile(language)
    # created file name for translateWords() function in order to open it in that function
    file_name = language + ".txt"
    # translate the english words to another language
    translateWords(englishList, secondList, file_name)
main()