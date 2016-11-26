from re import findall, compile
from nbu_decorators import todo_implement


def count_chars(string: str) -> dict:
    """ Return a dictionary containing all the chars
        from string as keys, and the number of time
        they appear as values.
        Example :
        >>> count_chars("Oh ! You're here !")
        {'Y': 1, 'o': 1, 'r': 2, 'O': 1, 'e': 3, "'": 1,
         'h': 2, '!': 2, 'u': 1, ' ': 4}
    """
    char_dic = {}
    for char in string:
        if char in char_dic.keys():
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic

@todo_implement
def count_words(string: str) -> dict:
    """ Return a dictionary containing all the words
        from string as keys, and the number of time
        they appear as values.
        Example :
        >>> count_words("Hello my friend.")
        {"Hello": 1, "my": 1, "friend": 1}
    """
    if not string:
        return {}

    regex = r"\b[a-zA-Z]+\b"
    regex = compile(regex)
    words_dic = {}

    return words_dic


def lower_chars_of_dict(dictionary: dict) -> None:
    """ Take a dict of chars as parameter, and change
        all of the upper keys from this dict to lower
        keys.
        Example :
        >>> lower_chars_of_dict({"a": 4, "A": 1, "B": 2})
        {"a": 5, "b": 2}
    """
    chars_to_lower = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
    for char in chars_to_lower:
        if char in dictionary.keys():
            if char.lower() in dict.keys():
                dictionary[char.lower()] += dictionary[char]
            else:
                dictionary[char.lower()] = dictionary[char]
            del dictionary[char]


def upper_chars_of_dict(dictionary: dict) -> None:
    """ Take a dict of chars as parameter, and change
        all of the lower keys from this dict to upper
        keys.
        Example :
        >>> upper_chars_of_dict({"a": 4, "A": 1, "B": 2})
        {"A": 5, "B": 2}
    """
    chars_to_upper = "abcdefghijklmnopqrstuvwxyz"
    for char in chars_to_upper:
        if char in dictionary.keys():
            if char.upper() in dictionary.keys():
                dictionary[char.upper()] += dictionary[char]
            else:
                dictionary[char.upper()] = dictionary[char]
            del dictionary[char]


def delete_chars_from_dict(chars_to_delete: str, dictionary: dict) -> None:
    """ Take a dict of chars as parameters and delete
        all his keys being presents in "chars_to_delete".
        Example :
        >>> delete_chars_from_dict("bA", {'a': 4, 'A': 2, 'b': 1})
        {'a': 4}
    """
    for char in chars_to_delete:
        if char in dictionary.keys():
            del dictionary[char]


if __name__ == "__main__":
    pass
