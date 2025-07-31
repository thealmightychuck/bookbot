from stats import get_num_words, get_chars_dict, counted_dict, list_values
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        print(len(sys.argv))
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        print(book_path)
        #sys.exit(0)

    print("============ BOOKBOT ============")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counted = get_chars_dict(text)
    counted_dict(counted)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()