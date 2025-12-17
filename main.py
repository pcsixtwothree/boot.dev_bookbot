from stats import num_words, num_char

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    #print(file_contents)

def main():
    text = get_book_text()
    print(f"Found {num_words(text)} total words")
    print(num_char(text))

main()
