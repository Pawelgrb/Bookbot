


#count the amount of words in the file
def count_words(words):
    count = 0
    for word in words:
        count += 1  

    return count

#creates a list of all the characters in the file and counts them
def char_count(strings):
    char = {}
    texts= strings.lower()
    for text in texts:
        if text in char:
            char[text] +=1
        else:
            char[text] = 1
    return char


#creating a list of dic. Each dic corrisponds to a single key=value
def sort_on(char):
    return char['num']

def sort_char(char_dic):
    lst_dic = []
    for key, value in char_dic.items(): 
        new_dic = {"char": key, "num": value}
        lst_dic.append(new_dic)
    lst_dic.sort(reverse=True, key=sort_on)
    return lst_dic