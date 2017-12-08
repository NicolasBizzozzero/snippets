"""
Sources and references :
- https://docs.python.org/3/library/string.html
- https://pypi.python.org/pypi/python-string-utils
- https://grass.osgeo.org/grass72/manuals/libpython/_modules/script/utils.html
"""
import difflib
from unidecode import unidecode
import string
import random
import json
import re
import unicodedata


LETTERS_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
LETTERS_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS = LETTERS_LOWERCASE + LETTERS_UPPERCASE
DIGITS_OCTAL = "01234567"
DIGITS_DECIMAL = "0123456789"
DIGITS_HEXADECIMAL = "0123456789ABCDEF"
PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
WHITESPACES = " \t\n\r\x0b\x0c"

URL_RE = re.compile(
    r'^'
    r'([a-z-]+://)'  # scheme
    r'([a-z_\d-]+:[a-z_\d-]+@)?'  # user:password
    r'(www\.)?'  # www.
    r'((?<!\.)[a-z\d]+[a-z\d\.-]+\.[a-z]{2,6}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|localhost)'  # domain
    r'(:\d{2,})?'  # port number
    r'(/[a-z\d_%\+-]*)*'  # folders
    r'(\.[a-z\d_%\+-]+)*'  # file extension
    r'(\?[a-z\d_\+%-=]*)?'  # query string
    r'(#\S*)?'  # hash
    r'$',
    re.IGNORECASE
)
EMAIL_RE = re.compile(r'^[a-zA-Z\d\._\+-]+@([a-z\d-]+\.?[a-z\d-]+)+\.[a-z]{2,4}$')
CAMEL_CASE_TEST_RE = re.compile(r'^[a-zA-Z]*([a-z]+[A-Z]+|[A-Z]+[a-z]+)[a-zA-Z\d]*$')
CAMEL_CASE_REPLACE_RE = re.compile(r'([a-z]|[A-Z]+)(?=[A-Z])')
SNAKE_CASE_TEST_RE = re.compile(r'^[a-z]+([a-z\d]+_|_[a-z\d]+)+[a-z\d]+$')
SNAKE_CASE_TEST_DASH_RE = re.compile(r'^[a-z]+([a-z\d]+-|-[a-z\d]+)+[a-z\d]+$')
SNAKE_CASE_REPLACE_RE = re.compile(r'(_)([a-z\d])')
SNAKE_CASE_REPLACE_DASH_RE = re.compile('(-)([a-z\d])')
CREDIT_CARDS = {
    'VISA': re.compile(r'^4[0-9]{12}(?:[0-9]{3})?$'),
    'MASTERCARD': re.compile(r'^5[1-5][0-9]{14}$'),
    'AMERICAN_EXPRESS': re.compile(r'^3[47][0-9]{13}$'),
    'DINERS_CLUB': re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'),
    'DISCOVER': re.compile(r'^6(?:011|5[0-9]{2})[0-9]{12}$'),
    'JCB': re.compile(r'^(?:2131|1800|35\d{3})\d{11}$')
}
JSON_WRAPPER_RE = re.compile(r'^\s*\{\s*.*\s*\}\s*$', re.MULTILINE | re.DOTALL)
UUID_RE = re.compile(r'^[a-f\d]{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}$', re.IGNORECASE)
IP_RE = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
WORDS_COUNT_RE = re.compile(r'\W*[^\W_]+\W*', re.IGNORECASE | re.MULTILINE | re.UNICODE)
HTML_RE = re.compile(
    r'((<([a-z]+:)?[a-z]+[^>]*/?>)(.*?(</([a-z]+:)?[a-z]+>))?|<!--.*-->|<!doctype.*>)',
    re.IGNORECASE | re.MULTILINE | re.DOTALL
)
HTML_TAG_ONLY_RE = re.compile(
    r'(<([a-z]+:)?[a-z]+[^>]*/?>|</([a-z]+:)?[a-z]+>|<!--.*-->|<!doctype.*>)',
    re.IGNORECASE | re.MULTILINE | re.DOTALL
)


def count_chars(string: str) -> dict:
    """ Return a dictionary countaining all the characters in
        string as keys, and the number of time they appear as values.

        Example :
        >>> count_chars("Hans' hammer")
        {' ': 1, 'r': 1, 'm': 2, 'a': 2,
         'e': 1, 'h': 1, 's': 1, 'H': 1,
         'n': 1, "'": 1}
    """
    dict_of_chars = dict()
    for char in string:
        try:
            dict_of_chars[char] += 1
        except KeyError:
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


def remove_char_at(string: str, index: int) -> str:
    """ Return string minus the char at the place index.
        Example :
        >>> remove_char_at("Hello World !", 5)
        HelloWorld !
    """
    return string[:index] + string[index + 1:]


def is_a_palindrome(string: str) -> bool:
    """ Return True if string is a palindrome, False otherwise.
        A palindrome is a string which can be read the same both ways by
        ignoring punctuation, whitespaces and the case of the chars.
        Example :
        >>> is_a_palindrome("As I pee, sir, I see Pisa !")
        True
        >>> is_a_palindrome("I am not.")
        False
    """
    if len(string) == 0:
        return True

    i, j = 0, len(string) - 1
    while i != j:
        if j == i + 1:
            return string[i] == string[j]
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def concatenation(*strings: str) -> str:
    """ Return the concatenation of all str passed as input, or an empty
    string if nothing has been passed.
    """
    result = ""
    for string in strings:
        result = "{0}{1}".format(result, string)
    return result


def similarity(string1: str, string2: str) -> float:
    """ Return the percentage of similarity between two strings. """
    return difflib.SequenceMatcher(None, string1, string2).ratio()


def remove_accents(string: str) -> str:
    """ Remove all accents from a string.

    Examples :
    >>> remove_accents("Málaga")
    Malaga
    """
    return unidecode.unidecode(string)


def is_string(obj):
    """
    Checks if an object is a string.

    :param obj: Object to test.
    :return: True if string, false otherwise.
    :rtype: bool
    """
    try:  # basestring is available in python 2 but missing in python 3!
        return isinstance(obj, basestring)
    except NameError:
        return isinstance(obj, str)


def is_full_string(string):
    """
    Check if a string is not empty (it must contains at least one non space
    character).

    :param string: String to check.
    :type string: str
    :return: True if not empty, false otherwise.
    """
    return is_string(string) and string.strip() != ''


def is_url(string, allowed_schemes=None):
    """
    Check if a string is a valid url.

    Full url example: scheme://username:password@www.domain.com:8042/folder/
    subfolder/file.extension?param=value&param2=value2#hash

    :param string: String to check.
    :param allowed_schemes: List of valid schemes ('http', 'https', 'ftp'...).
           Default to None (any scheme is valid).
    :return: True if url, false otherwise
    :rtype: bool
    """
    if not is_full_string(string):
        return False
    valid = bool(URL_RE.search(string))
    if allowed_schemes:
        return valid and any([string.startswith(s) for s in allowed_schemes])
    return valid


def is_email(string):
    """
    Check if a string is an email.

    | **IMPORTANT NOTES**:
    | By design, the implementation of this checking does not follow the
    specification for a valid email address, but instead it's based on real
    world cases in order to match more than 99% of emails and catch user
    mistakes. For example the percentage sign "%" is a valid sign for an
    email, but actually no one use it, instead if such sign is found in a
    string coming from user input (like a web form) is very likely that the
    intention was to type "5" (which is on the same key on a US keyboard).

    :param string: String to check.
    :type string: str
    :return: True if email, false otherwise.
    :rtype: bool
    """
    return is_full_string(string) and bool(EMAIL_RE.search(string))


def is_credit_card(string, card_type=None):
    """
    Checks if a string is a valid credit card number.
    If card type is provided then it checks that specific type,
    otherwise any known credit card number will be accepted.

    :param string: String to check.
    :type string: str
    :param card_type: Card type.
    :type card_type: str

    Can be one of these:

    * VISA
    * MASTERCARD
    * AMERICAN_EXPRESS
    * DINERS_CLUB
    * DISCOVER
    * JCB

    or None. Default to None (any card).

    :return: True if credit card, false otherwise.
    :rtype: bool
    """
    if not is_full_string(string):
        return False
    if card_type:
        if card_type not in CREDIT_CARDS:
            raise KeyError(
                ('Invalid card type "{}".\
                 Valid types are: {}').format(card_type,
                 ', '.join(CREDIT_CARDS.keys()))
            )
        return bool(CREDIT_CARDS[card_type].search(string))
    for c in CREDIT_CARDS:
        if CREDIT_CARDS[c].search(string):
            return True
    return False


def is_camel_case(string):
    """
    Checks if a string is formatted as camel case.
    A string is considered camel case when:

    - it's composed only by letters ([a-zA-Z]) and optionally numbers ([0-9])
    - it contains both lowercase and uppercase letters
    - it does not start with a number


    :param string: String to test.
    :type string: str
    :return: True for a camel case string, false otherwise.
    :rtype: bool
    """
    return is_full_string(string) and bool(CAMEL_CASE_TEST_RE.search(string))


def is_snake_case(string, separator='_'):
    """
    Checks if a string is formatted as snake case.
    A string is considered snake case when:

    * it's composed only by lowercase letters ([a-z]), underscores (or
    provided separator) and optionally numbers ([0-9])
    * it does not start/end with an underscore (or provided separator)
    * it does not start with a number


    :param string: String to test.
    :type string: str
    :param separator: String to use as separator.
    :type separator: str
    :return: True for a snake case string, false otherwise.
    :rtype: bool
    """
    if is_full_string(string):
        re_map = {
            '_': SNAKE_CASE_TEST_RE,
            '-': SNAKE_CASE_TEST_DASH_RE
        }
        re_template = '^[a-z]+([a-z\d]+{sign}|{sign}[a-z\d]+)+[a-z\d]+$'
        r = re_map.get(separator,
            re.compile(re_template.format(sign=re.escape(separator))))
        return bool(r.search(string))
    return False


def is_json(string):
    """
    Check if a string is a valid json.

    :param string: String to check.
    :type string: str
    :return: True if json, false otherwise
    :rtype: bool
    """
    if not is_full_string(string):
        return False
    if bool(JSON_WRAPPER_RE.search(string)):
        try:
            return isinstance(json.loads(string), dict)
        except (TypeError, ValueError, OverflowError):
            return False
    return False


def is_ip(string):
    """
    Checks if a string is a valid ip.

    :param string: String to check.
    :type string: str
    :return: True if an ip, false otherwise.
    :rtype: bool
    """
    return is_full_string(string) and bool(IP_RE.search(string))


def is_pangram(string):
    """
    Checks if the string is a pangram (https://en.wikipedia.org/wiki/Pangram).

    :param string: String to check.
    :type string: str
    :return: True if the string is a pangram, False otherwise.
    """
    return is_full_string(string) and\
           set(SPACES_RE.sub('', string)).issuperset(set(LETTERS_LOWERCASE))


def is_isogram(string):
    """
    Checks if the string is an isogram (https://en.wikipedia.org/wiki/Isogram).

    :param string: String to check.
    :type string: str
    :return: True if isogram, false otherwise.
    """
    return is_full_string(string) and len(set(string)) == len(string)


def is_slug(string, sign='-'):
    """
    Checks if a given string is a slug.

    :param string: String to check.
    :type string: str
    :param sign: Join sign used by the slug.
    :type sign: str
    :return: True if slug, false otherwise.
    """
    if not is_full_string(string):
        return False
    rex = r'^([a-z\d]+' + re.escape(sign) + r'?)*[a-z\d]$'
    return re.match(rex, string) is not None


def words_count(string):
    """
    Returns the number of words contained into the given string.

    This method is smart, it does consider only sequence of one or more
    letter and/or numbers as "words", so a string like this: "! @ # % ... []"
    will return zero! Moreover it is aware of punctuation, so the count for a
    string like "one,two,three.stop" will be 4 not 1 (even if there are no
    spaces in the string).

    :param string: String to check.
    :type string: str
    :return: Number of words.
    :rtype: int
    """
    return len(WORDS_COUNT_RE.findall(string))


def contains_html(string):
    """
    Checks if the given string contains html code.
    By design, this function is very permissive regarding what to consider
    html code, don't expect to use it as an html validator, its goal is to
    detect "malicious" or undesired html tags in the text.

    :param string: Text to check
    :type string: str
    :return: True if string contains html, false otherwise.
    :rtype: bool
    """
    return bool(HTML_RE.search(string))


def camel_case_to_snake(string, separator='_'):
    """
    Convert a camel case string into a snake case one.
    (The original string is returned if is not a valid camel case string)

    :param string: String to convert.
    :type string: str
    :param separator: Sign to use as separator.
    :type separator: str
    :return: Converted string.
    :rtype: str
    """
    if not is_string(string):
        raise TypeError('Expected string')
    if not is_camel_case(string):
        return string
    return CAMEL_CASE_REPLACE_RE.sub(lambda m: m.group(1) + separator,
        string).lower()


def snake_case_to_camel(string, upper_case_first=True, separator='_'):
    """
    Convert a snake case string into a camel case one.
    (The original string is returned if is not a valid snake case string)

    :param string: String to convert.
    :type string: str
    :param upper_case_first: True to turn the first letter into uppercase
                             (default).
    :type upper_case_first: bool
    :param separator: Sign to use as separator (default to "_").
    :type separator: str
    :return: Converted string
    :rtype: str
    """
    if not is_string(string):
        raise TypeError('Expected string')
    if not is_snake_case(string, separator):
        return string
    re_map = {
        '_': SNAKE_CASE_REPLACE_RE,
        '-': SNAKE_CASE_REPLACE_DASH_RE
    }
    r = re_map.get(separator,
        re.compile('({sign})([a-z\d])'.format(sign=re.escape(separator))))
    string = r.sub(lambda m: m.group(2).upper(), string)
    if upper_case_first:
        return string[0].upper() + string[1:]
    return string


def shuffle(string):
    """
    Return a new string containing shuffled items.

    :param string: String to shuffle
    :type string: str
    :return: Shuffled string
    :rtype: str
    """
    s = sorted(string)  # turn the string into a list of chars
    random.shuffle(s)  # shuffle the list
    return ''.join(s)  # convert the shuffled list back to string


def diff_files(filename_a, filename_b):
    """Diffs two text files and returns difference.

    :param str filename_a: first file path
    :param str filename_b: second file path

    :return: list of strings
    """
    with open(filename_a) as file_a, open(filename_b) as file_b: 

        return list(difflib.Differ().compare(file_a.readlines(),
                                             file_b.readlines()))


def leading_zeros(number: int, number_of_digits_wanted: int) -> str:
    """ Return a number with as many zeros as necessary to match
    `number_of_digits_wanted`.
    """
    return str(number).zfill(number_of_digits_wanted)


if __name__ == '__main__':
    pass
