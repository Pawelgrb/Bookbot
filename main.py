from stats import count_words


#function that reads the file
def get_book_text(path_file):
    with open(path_file) as f:
        file_contents = f.read()

    return file_contents


def main():
    # get the file path
    book = get_book_text("books/frankenstein.txt")
    words = book.split()
    num_words = count_words(words)
    print(num_words, "words found in the document")

 
main()