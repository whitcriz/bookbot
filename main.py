import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    num_words = count_words(file_contents)
    num_characters = count_characters(file_contents)
    sorted_characters = sort_characters(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_characters:
        character = dict["char"]
        count = dict["num"]
        if (character.isalpha()):
            print(f"{character}: {count}")
    print("============= END ===============")


main()

