def number_of_words(book_contents):
    """
    Takes the book content as a string and returns number of words

    Args:
        book_contents (str): Book as a string

    Returns:
        int: The number of words
    """
    num = book_contents.split()
    return len(num)


def character_count(book_contents):
    """
    Takes book contents and returns dict of each character and its count in the contents

    Args:
        book_contents (str) : book as a string

    Returns:
        dict{str: int} A dict of each character in book contents and the count of that character

    """
    char_dict = {}
    for word in book_contents:
        for letter in word:
            lower_letter = letter.lower()
            if lower_letter in char_dict:
                char_dict[lower_letter] += 1
            else:
                char_dict[lower_letter] = 1

    return char_dict


def sort_character_dict(character_dict):
    """
    Takes character dict and returns a sorted list of dicts containing character and count

    Args:
        character_dict  dict{str:int}: Dictionary of characters and their count

    Returns:
        sorted list of dicts {character: str, count: int}
    """
    sorted_list = []
    for k, v in character_dict.items():
        sorted_list.append({"character": k, "count": v})

    sorted_list.sort(reverse=True, key=lambda x: x["count"])
    return sorted_list
