def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    #print(file_contents)

def main():
    get_book_text()
    print(f"Found {num_words(get_book_text())} total words")

def num_words(book):
    words = book.split()
    return len(words)

    
main()
