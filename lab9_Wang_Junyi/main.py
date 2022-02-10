# Junyi, carsonw@usc.edu
# ITP 115, Fall 2021
# Section: Bagel
# Lab 9

# define function: read_file
# parameter 1: user_genre
# parameter 2: file_name a default value of "shows.cvs"
# return value: a list of shows where the user's genre is inside of the show's genre
def read_file(user_genre, file_name="shows.csv"):
    show_list = []
    file_read = open(file_name, "r")
    for line in file_read:
        line = line.strip()  # get rid of \n
        # list = str.split(sep)
        line_list = line.split(",")
        show_title = line_list[0]
        show_genre = line_list[1]
        if user_genre in show_genre:
            show_list.append(show_title)

    file_read.close()
    return show_list

# function: write_file
# parameter 1: genre
# parameter 2: show_list
# return value: None
def write_file(genre, show_list):
    name_file = genre + ".txt"
    file_write = open(name_file, "w")
    for show in show_list:
        print(show, file=file_write)

    file_write.close()

def main():
    print("TV Shows")
    genre_str = "action & adventure, animation, comedy, documentary, drama, mystery & suspense, science fiction & fantasy"
    print("Possible genres are", genre_str)
    user_genre = input("Enter a genre: ")
    while user_genre not in genre_str:  # loop while bad input
        user_genre = input("Enter a genre: ")

    # we have a good user_genre
    tv_shows = read_file(user_genre)
    write_file(user_genre, tv_shows)
    print("The file '" + user_genre + ".txt' has the following shows:")
    print(tv_shows)

main()



