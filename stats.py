


#count the amount of words in the file
def count_words(words):
    count = 0
    for word in words:
        count += 1  

    return count

def char_count(strings):
    char = {}
    texts= strings.lower()
    for text in texts:
        if text in char:
            char[text] +=1
        else:
            char[text] = 1
    return char