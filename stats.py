def get_book_text(path):
    print(f"Analyzing book found at {path}...")
    with open(path, encoding="utf-8") as file:
        return file.read()

def get_num_words():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = 0
    words = book_text.split()
    num_words = len(words)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def get_num_characters():
    book_text = get_book_text("books/frankenstein.txt")
    num_characters = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in num_characters:
            num_characters[lowered] += 1
        elif lowered.isalpha():
            num_characters[lowered] = 1
    return num_characters

def sort_by_number():
    print("----------- Character Count ----------")
    num_characters = get_num_characters()
    sorted_tuples = sorted(num_characters.items(), key=lambda x: x[1], reverse=True)
    sorted_characters = [{"char": char, "num": count} for char, count in sorted_tuples]
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")