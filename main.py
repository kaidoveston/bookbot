import sys

from stats import word_count, char_counts, sort_counts

def get_book_text(file_name):
    with open(file_name) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    count = word_count(text)
    print(f"{count} words found in the document")
    counts = char_counts(text)
    counts = sort_counts(counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for count in counts:
        if count["char"].isalpha():
            print(f"{count['char']}: {count['num']}")
    print("============= END ===============")

main()
