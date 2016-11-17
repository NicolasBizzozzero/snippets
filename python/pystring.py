def get_dictionary_counting_all_chars_of(str):
    dict_of_chars = dict()

    for char in str:
        if char in dict_of_chars:
            dict_of_chars[char] += 1
        else:
            dict_of_chars[char] = 1

    return dict_of_chars


def reverse(str):
    return str[::-1]
    pass


def is_a_palindrome(string: str) -> bool:
    """Return True if string is a palindrome, False otherwise.
        A palindrome is a string who can be read the same both
        ways.
    """
    return string == ''.join(reversed(string))


if __name__ == '__main__':
    pass
