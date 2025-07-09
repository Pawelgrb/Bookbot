from stats import *
import sys

#function that reads the file
def get_book_text(path_file):
    with open(path_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    # get the file path and calculation from stats.py
    path_length = len(sys.argv)
    if path_length > 1:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(path)
    words = book.split()
    num_words = count_words(words)
    characters = char_count(book)
    sort_characters = sort_char(characters)
    print("============ BOOKBOT ============ ")
    print("Analyzing book found at", path)
    print("----------- Word Count ----------")
    print("Found",num_words, "total words")
    print("--------- Character Count -------")
    for character_dict in sort_characters:
        if character_dict["char"].isalpha():
            print(character_dict["char"] + ": " + str(character_dict["num"]))
    print("============= END ===============")

 
main()