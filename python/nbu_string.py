def get_a_dictionary_counting_all_chars_of(string: str) -> dict:
    """ Return a dictionary countaining all the characters in
        string as keys, and the number of time they appear as values.
        Example :
        >>> get_a_dictionary_counting_all_chars_of("Hans' hammer")
        {' ': 1, 'r': 1, 'm': 2, 'a': 2,
         'e': 1, 'h': 1, 's': 1, 'H': 1,
         'n': 1, "'": 1}
    """
    dict_of_chars = dict()
    for char in string:
        if char in dict_of_chars:
            dict_of_chars[char] += 1
        else:
            dict_of_chars[char] = 1
    return dict_of_chars


def reversed(string: str) -> str:
    """ Return the string reversed.
        Example :
        >>> reversed("Hello World !")
        ! dlroW olleH
    """
    return string[::-1]


def remove_chars(string: str, chars_to_remove: str) -> str:
    """ Return string without the chars contained in chars_to_remove.
        Example :
        >>> remove_chars("Hello World !", " o!e")
        HllWrld
    """
    new_string = string
    chars_removed = 0
    for index, char in enumerate(string):
        for char_to_remove in chars_to_remove:
            if char == char_to_remove:
                new_string = remove_char_at(new_string, index - chars_removed)
                chars_removed += 1
                break
    return new_string


def remove_chars_which_are_not_letters(string: str, keep_numbers: bool = True,
                                       keep_whitespaces: bool = True) -> str:
    """ Return only the chars contained in string.
        Example :
        >>> remove_chars_which_are_not_letters("Hello, World!")
        Hello World
        >>> remove_chars_which_are_not_letters("I'm 21 years old.",
                                                False, False)
        Imyearsold
    """
    chars_to_keep = "abcdefghijklmnopqrstuvwxyz"
    if keep_numbers:
        chars_to_keep = "{}0123456789".format(chars_to_keep)
    if keep_whitespaces:
        chars_to_keep = "{} \n\t".format(chars_to_keep)

    chars_removed = 0
    new_string = string
    for index, char in enumerate(string):
        if char.lower() not in chars_to_keep:
            new_string = remove_char_at(new_string, index - chars_removed)
            chars_removed += 1
    return new_string


def remove_char_at(string: str, index: int) -> str:
    """ Return string minus the char at the place index.
        Example :
        >>> remove_char_at("Hello World !", 5)
        HelloWorld !
    """
    return string[:index] + string[index + 1:]


def is_a_palindrome(string: str) -> bool:
    """ Return True if string is a palindrome, False otherwise.
        A palindrome is a string who can be read the same both ways by
        ignoring punctuation, whitespaces and the case of the chars.
        Example :
        >>> is_a_palindrome("As I pee, sir, I see Pisa !")
        True
        >>> is_a_palindrome("I am not.")
        False
    """
    return remove_chars_which_are_not_letters(string, True, False).lower() ==\
        ''.join(reversed(remove_chars_which_are_not_letters(string,
                                                            True,
                                                            False)).lower())


def concatenation(*strings: str) -> str:
    """ Return the concatenation of all str passed as input, or an empty string
    if nothing has been passed.
    """
    result = ""
    for string in strings:
        result = "{}{}".format(result, string)
    return result


if __name__ == '__main__':
    pass
