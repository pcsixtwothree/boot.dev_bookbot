from stats import num_words, num_char, sorting, abc

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    #print(file_contents)

def main():
    text = get_book_text()
    print(f"Found {num_words(text)} total words")
    #print(num_char(text))
    #print(sorting(num_char(text)))
    sort_list = sorting(num_char(text))
    for char_dict in sort_list:
        temp_char = char_dict["char"]
        if temp_char.isalpha():
            char = char_dict["char"]
            num = char_dict["num"]
            print(f"{char_dict["char"]}: {char_dict["num"]}")

main()
