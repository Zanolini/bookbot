def get_book_text(path):
    with open(path, encoding="utf-8") as file:
        return file.read()

def get_num_words():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = 0
    words = book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def get_num_characters():
    book_text = get_book_text("books/frankenstein.txt")
    num_characters = {}
    for char in book_text:
        if char in num_characters:
            num_characters[char] += 1
        else:
            num_characters[char] = 1
    print(num_characters)