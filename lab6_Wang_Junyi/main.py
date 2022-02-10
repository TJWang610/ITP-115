def get_languages(file_name="languages.csv"):
    # open the file
    languages = open(file_name, "r")
    header = languages.readline()
    header = header.strip()
    header_lang = header.split(",")
    languages.close()
    return header_lang

# Define the getTranslationLanguage(langList) function.
# o Parameter: langList is a list of the languages
# o Return value: a string for the language to translate words into

def get_translation_language(lang_list):
    lang_list = ["Danish", "Dutch", "Finnish", "French", "German", "Indonesian", "Italian",
                "Japanese", "Latin", "Norwegian", "Portuguese", "Spanish", "Swahili", "Swedish"]
    print("Translate English words to one of the following languages:\n",
          "Danish", "Dutch", "Finnish", "French", "German", "Indonesian", "Italian\n",
                "Japanese", "Latin", "Norwegian", "Portuguese", "Spanish", "Swahili", "Swedish")
    lang = input("Enter a language: ").capitalize()
    while lang not in lang_list:
        print("This program does not support", lang.capitalize())
        lang = input("Enter a language: ").capitalize()
    return lang.capitalize()

# Define the readFile(langList, langStr, fileName) function.
# o Parameter 1: langList is a list of the languages
# o Parameter 2: langStr is a string of containing the name of a language and it has
# a default value of "English"
# o Parameter 3: fileName is a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# o Return value: a list of words in the language identified by the langStr parameter


def read_file(lang_list, lang_str, file_name="languages.csv"):
    # Create an empty list.
    list = []
    # o Open the CSV file and read the header row to skip it.
    fin = open(file_name, "r")
    header_line = fin.readline()
    # o Use the langList and langStr parameters to determine the index of the language.
    language_index = lang_list.index(lang_str)
    # o Loop through the rest of the file. Each line of data will have an extraneous new
    # line at the end
    for line in fin:
        line = line.strip() # remove
        line = line.split(",") # break up the line into a list of strings
        translation = line[language_index]
        list.append(translation) # Get the correct word and append it to the list.
    fin.close()
    return list

# Define the createResultsFile(language) function.
# o Parameter: language is a string containing the name of the language for
# translation
# o Return value: None


def create_results_file(language):
    name_file = language + ".txt"
    out_file = open(name_file, "w")
    print("Words translated from English to", language, file=out_file)
    # print(language, file=out_file)
    out_file.close()

# Define the translateWords(englishList, translationList, language) function.
# o Parameter 1: englishList is a list of words in English
# o Parameter 2: translationList is a list of words in another language (not English)
# o Parameter 3: language is a string containing the language of the words in the
# translationList
# o Return value: none

def translate_words(english_list, translation_list, language):
    # open the results file
    name_file = language + ".txt"
    out_file = open(name_file, "w")
    continue_translator = "y"
    # ask user to enter an english word to translate

    while continue_translator.lower() == "y":
        enter = input("\nEnter a word to translate: ").lower()
        indexed = english_list.index(enter)
        translation = translation_list[indexed]
        if enter not in english_list:
            print(enter, "is not in the English list")
            continue_translator = input("Another word (y or n) ")
            # put this before a valid translation, not "-"
        elif enter in english_list and translation == "-": 
            print(enter, "does not have a translation")
            continue_translator = input("Another word (y or n) ")
        elif enter in english_list:
            print(enter, "is translated to", translation)
            print(enter, "=", translation, file=out_file)
            continue_translator = input("Another word (y or n) ")

        # if the word is not in the english list, tell the user

    print("\nTranslated words have been saved to", name_file)

# translate the word. if there is a translation, show the user
# if there is no translation, tell the user
# then ask if they want to translate the word


def main():
    print("Language Translator")
    display = get_languages("../lab7_Wang_Junyi/languages.csv")
    translate = read_file(display, lang_str="English", file_name="../lab7_Wang_Junyi/languages.csv")
    translated_lang = get_translation_language(display)
    trans_lang_one = read_file(display, lang_str=translated_lang, file_name="../lab7_Wang_Junyi/languages.csv")
    create_results_file(translated_lang)
    translate_words(translate, trans_lang_one, translated_lang)



main()
