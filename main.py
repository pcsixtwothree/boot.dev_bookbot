from stats import num_words, num_char, sorting, abc
import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents
    #print(file_contents)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text()
    print(f"Found {num_words(text)} total words")
    #print(num_char(text))
    #print(sorting(num_char(text)))
    sort_list = sorting(num_char(text))
    for char_dict in sort_list:
        temp_char = char_dict["char"]
        if temp_char.isalpha():
            #char = char_dict["char"] # not used anymore it's just here to haunt me
            #num = char_dict["num"]
            print(f"{char_dict["char"]}: {char_dict["num"]}")

main()
