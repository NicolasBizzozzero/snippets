from nbu_string import concatenation
from nbu_dict import count_chars as count_chars_from_str
from math import inf as infinity


def get_content(filepath: str) -> str:
    """ Return the content of a file. """
    string = ""
    with open(filepath) as file:
        string = file.read()
    return string


def create_file(filepath: str, content: str = "") -> None:
    """ Create a file with an optional content.
        /!\ WARNING : If a file with the same name already exists, this
        function will overwrite it.
    """
    overwrite_content_in_a_file(filepath, content)


def overwrite_content_in_a_file(filepath: str, new_content: str) -> None:
    """ Write content inside a file and overwrite its previous content. """
    with open(filepath, 'w') as file:
        file.write(new_content)


def append_content_in_a_file(filepath: str, content_to_append: str) -> None:
    """ Write content inside a file whitout overwriting its previous
        content.
    """
    with open(filepath, 'a') as file:
        file.write(content_to_append)


def erase_content_of_a_file(filepath: str) -> None:
    """ Erase the content of a file. """
    with open(filepath, 'w') as file:
        file.write("")


def copy_file(filepath: str, copy_filepath: str) -> None:
    """ Paste the content from a file inside another file. Overwrite its content
        if he exists, or create it with the duped content otherwise.
    """
    content = get_content(filepath)
    overwrite_content_in_a_file(copy_filepath, content)


def get_number_of_lines(filepath: str) -> int:
    """ Return the number of lines contained inside file. """
    number_of_lines = 0
    with open(filepath) as file:
        for line in file:
            number_of_lines += 1
    return number_of_lines


def count_chars(filepath: str) -> dict:
    """ Return a dictionary containing all the chars
        from file as keys, and the number of time
        they appear in this file as values.
        Example :
        >>> count_chars("file.txt")
        {'Y': 1, 'o': 1, 'r': 2, 'O': 1, 'e': 3, "'": 1,
         'h': 2, '!': 2, 'u': 1, ' ': 4}
    """
    return count_chars_from_str(get_content(filepath))


def get_line(filepath: str, line_number: int) -> str:
    """ Return the content of file at the line indicated by line_number. Return
        an empty string if line_number outreach the actual number of lines in
        file.
    """
    if line_number <= 0:
        return ""
    current_index = 0
    with open(filepath) as file:
        for line in file:
            current_index += 1
            if current_index == line_number:
                return line
    # If we are here, then the file has a number of lines inferior
    # to line_number
    return ""


def get_lines(filepath: str, floor: int, ceil: int) -> str:
    """ Return the content of file between the lines indicated by floor
        (inclusive) and ceil (exclusive). Return an empty string if line_number
        outreach the actual number of lines in file.
    """
    content = ""
    current_line = 1
    with open(filepath) as file:
        for line in file:
            if current_line >= ceil:
                break
            if current_line >= floor:
                content = concatenation(content, line)
            current_line += 1
    return content


def get_all_content_after(filepath: str, line_number: int) -> str:
    """ Get the lines of filepath from line_number (exclusive). """
    return get_lines(filepath, line_number + 1, infinity)


def get_all_content_before(filepath: str, line_number: int) -> str:
    """ Get the lines of filepath from line_number (exclusive). """
    return get_lines(filepath, -infinity, line_number)


def get_first_line(filepath: str) -> str:
    """ Get the first line from filepath. """
    return get_all_content_before(filepath, 2)


def get_last_line(filepath: str) -> str:
    """ Get the last line from filepath. """
    with open(filepath) as file:
        return file.readlines()[-1]


def delete_line(filepath: str, line_number: int,
                replace_by_blank_line: bool = False) -> None:
    """ Delete the line from filepath indicated by line_number. """
    if line_number <= 0:
        return
    current_index = 0
    content = ""
    with open(filepath) as file:
        for line in file:
            current_index += 1
            if current_index == line_number:
                # We need to delete this line
                if replace_by_blank_line:
                    content = concatenation(content, "\n")
                continue
            content = concatenation(content, line)

    # Replace the file with a copy of itself without the line to delete
    overwrite_content_in_a_file(filepath, content)


def delete_lines(filepath: str, floor: int, ceil: int,
                 replace_by_blank_lines: bool = False) -> None:
    """ Delete the lines from filepath indicated by floor (inclusive) and
        ceil (exclusive).
    """
    # Exit in impossible cases
    if (floor >= ceil) or (ceil <= 1):
        return
    current_index = 0
    content = ""
    with open(filepath) as file:
        for line in file:
            current_index += 1
            if floor <= current_index < ceil:
                # We need to delete this line
                if replace_by_blank_lines:
                    content = concatenation(content, "\n")
                continue
            content = concatenation(content, line)

    # Replace the file with a copy of itself without the lines to delete
    overwrite_content_in_a_file(filepath, content)


def delete_all_content_after(filepath: str, line_number: int) -> None:
    """ Delete the lines of filepath from line_number (exclusive). """
    delete_lines(filepath, line_number + 1, infinity)


def delete_all_content_before(filepath: str, line_number: int) -> None:
    """ Delete the lines of filepath from line_number (exclusive). """
    delete_lines(filepath, -infinity, line_number)


def delete_first_line(filepath: str) -> None:
    """ Delete the first line from filepath. """
    delete_all_content_before(filepath, 2)


def delete_last_line(filepath: str) -> None:
    """ Delete the last line from filepath. """
    # Get all the content before the last line
    content = None
    with open(filepath) as file:
        content = "".join(file.readlines()[:-1])

    # Replace the file with a copy of itself without the line to delete
    overwrite_content_in_a_file(filepath, content)


def extract_line(filepath: str, line_number: int,
                 replace_by_blank_line: bool = False) -> str:
    """ Extract the line from filepath indicated by line_number. """
    if line_number <= 0:
        return
    current_index = 0
    content = ""
    line_to_extract = None
    with open(filepath) as file:
        for line in file:
            current_index += 1
            if current_index == line_number:
                # We need to delete this line
                if replace_by_blank_line:
                    content = concatenation(content, "\n")
                line_to_extract = line
                continue
            content = concatenation(content, line)

    # Replace the file with a copy of itself without the line to delete
    overwrite_content_in_a_file(filepath, content)

    return line_to_extract


def extract_lines(filepath: str, floor: int, ceil: int,
                  replace_by_blank_lines: bool = False) -> str:
    """ Extract the lines from filepath indicated by floor (inclusive) and
        ceil (exclusive).
    """
    # Exit in impossible cases
    if (floor >= ceil) or (ceil <= 1):
        return
    current_index = 0
    content = ""
    lines_to_extract = None
    with open(filepath) as file:
        for line in file:
            current_index += 1
            if floor <= current_index < ceil:
                # We need to delete this line
                if replace_by_blank_lines:
                    content = concatenation(content, "\n")
                lines_to_extract = concatenation(lines_to_extract, line)
                continue
            content = concatenation(content, line)

    # Replace the file with a copy of itself without the lines to extract
    overwrite_content_in_a_file(filepath, content)

    return lines_to_extract


def extract_all_content_after(filepath: str, line_number: int) -> str:
    """ Extract the lines of filepath from line_number (exclusive). """
    return extract_lines(filepath, line_number + 1, infinity)


def extract_all_content_before(filepath: str, line_number: int) -> str:
    """ Extract the lines of filepath from line_number (exclusive). """
    return extract_lines(filepath, -infinity, line_number)


def extract_first_line(filepath: str) -> str:
    """ Extract the first line from filepath. """
    return extract_all_content_before(filepath, 2)


def extract_last_line(filepath: str) -> str:
    """ Extract the last line from filepath. """
    # Get all the content before the last line
    content = None
    last_line = None
    with open(filepath) as file:
        content = file.readlines()
    last_line = content[-1]
    content = "".join(content[:-1])

    # Replace the file with a copy of itself without the line to extract
    overwrite_content_in_a_file(filepath, content)

    return last_line


if __name__ == '__main__':
    pass
