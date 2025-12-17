def num_words(book):
    words = book.split()
    return len(words)

def num_char(string):
    char_dict = {}
    l_string = string.lower()
    for char in l_string:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict