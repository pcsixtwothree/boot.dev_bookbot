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

def helper_dict(dict):
    return dict["num"]

def sorting(dict):
    uns_list = []
    for k, v in dict.items():
        uns_list.append({"char": k , "num": v})
    uns_list.sort(reverse=True, key=helper_dict)
    return uns_list

def abc(list):
    abc_list = []
    for dict in list:
        if dict["char"].isalpha():
            abc_list.append(dict)
        continue
    return abc_list
