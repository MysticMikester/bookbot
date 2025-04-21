from stats import count_words, count_chars, sort_chars
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
        num_words = count_words(text)
        num_chars = count_chars(text)
        sorted_chars = sort_chars(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words in the document")
        print("--------- Character Count -------")
        for item in sorted_chars:
            print(f"{item['char']}: {item['count']}")
        print("============= END ===============")



main ()
