from stats import count_words, char_count, chars_list
import sys 

# def get_book_text(textfile):
#     with open(textfile) as f:
#         file_contents = f.read()
#     return file_contents

# def main():
#     return get_book_text("./books/frankenstein.txt")


# num_words = count_words(main())
# print(f"Found {num_words} total words")

# # print(sort_on(char_count(main())))
# print(sort_on(main()))



def main(path_to_book):
    # book_path = "books/frankenstein.txt"
    book_path = path_to_book
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = char_count(text)
    chars_sorted_list = chars_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])