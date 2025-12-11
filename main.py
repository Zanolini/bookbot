from stats import get_num_words, get_num_characters, sort_by_number 
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    get_num_words(sys.argv[1])
    get_num_characters(sys.argv[1])
    sort_by_number(sys.argv[1])

main()