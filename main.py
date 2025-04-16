import sys

from stats import number_of_words, character_count, sort_character_dict


def get_book_text(filepath):
    """
    Reads the content of a book from a file and returns it as a string.

    Args:
        filepath (str): The filepath to the book file.

    Returns:
        str: The content of the book.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def print_report(wc, char_count_list, book_path):
    """
    Takes Word Count and Character Count Dict and prints report on book

    Args:
        wc (int): Word Count of the book
        char_count_list (List[dict]): A list of dicts containing character and counts
        book_path (str): Path to book

    Returns:
        None
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for character in char_count_list:
        if character["character"].isalpha():
            print(f"{character["character"]}: {character["count"]}")
    print("============= END ===============")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    contents = get_book_text(book_path)
    word_count = number_of_words(contents)
    char_count = character_count(contents)
    sorted_list = sort_character_dict(char_count)
    print_report(word_count, sorted_list, book_path)


main()