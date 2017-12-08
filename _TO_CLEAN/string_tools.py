import difflib
import unidecode


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
