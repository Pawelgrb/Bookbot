from stats import *


#function that reads the file
def get_book_text(path_file):
    with open(path_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    # get the file path and calculation from stats.py
    print("============ BOOKBOT ============ ")
    print("Analyzing book found at books/frankenstein.txt...")
    book = get_book_text("books/frankenstein.txt")
    words = book.split()
    num_words = count_words(words)
    characters = char_count(book)
    sort_characters = sort_char(characters)
    print("----------- Word Count ----------")
    print("Found",num_words, "total words")
    print("--------- Character Count -------")
    for character_dict in sort_characters:
        if character_dict["char"].isalpha():
            print(character_dict["char"] + ": " + str(character_dict["num"]))
    print("============= END ===============")

 
main()