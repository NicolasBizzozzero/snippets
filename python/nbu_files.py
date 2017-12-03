from nbu_string import concatenation
from nbu_dict import count_chars as count_chars_from_str
from math import inf as infinity
import os
import sys
import errno


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


def is_file_existing(filename: str) -> bool:
    """ Return True if the file exists, False otherwise. """
    import os.path
    return os.path.isfile(filename)


def get_extension(filename: str) -> str:
    """ Return the extension of a file without the dot.

        Examples :
        >>> get_extension("hello_world.py")
        py
        >>> get_extension("hello_world")

        >>> get_extension("hello_world.txt.py")
        py
        >>> get_extension("hello_world.txt.c.py")
        py
    """
    import os
    return os.path.splitext(filename)[1][1:]


def get_size(filepath: str) -> int:
    """ Return the size of a file, in bytes. """
    import os
    return os.stat(filepath).ST_SIZE


def tail(path: str, encoding: str = "utf8"):
    with open(path, "rb") as file:
        file.seek(-2, os.SEEK_END)    # Jump to the second last byte.
        while file.read(1) != b"\n":  # Until EOL is found...
                                      # ...jump back the read byte plus one more
            file.seek(-2, os.SEEK_CUR)
        last = file.readline()       # Read last line.
    return last.decode(encoding)


def is_pathname_valid(pathname: str) -> bool:
    """ `True` if the passed pathname is a valid pathname for the current OS,
    `False` otherwise.
    Shamelessly pasted from https://stackoverflow.com/a/34102855
    """
    # Windows-specific error code indicating an invalid pathname.
    # See also :
    # https://msdn.microsoft.com/en-us/library/windows/desktop/ms681382%28v=vs.85%29.aspx
    ERROR_INVALID_NAME = 123

    # If this pathname is either not a string or is but is empty, this pathname
    # is invalid.
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
        # if any. Since Windows prohibits path components from containing `:`
        # characters, failing to strip this `:`-suffixed prefix would
        # erroneously invalidate all valid absolute Windows pathnames.
        _, pathname = os.path.splitdrive(pathname)

        # Directory guaranteed to exist. If the current OS is Windows, this is
        # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
        # environment variable); else, the typical root directory.
        root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else os.path.sep
        assert os.path.isdir(root_dirname)   # ...Murphy and her ironclad Law

        # Append a path separator to this directory if needed.
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        # Test whether each path component split from this pathname is valid or
        # not, ignoring non-existent and non-readable path components.
        for pathname_part in pathname.split(os.path.sep):
            try:
                os.lstat(root_dirname + pathname_part)
            # If an OS-specific exception is raised, its error code
            # indicates whether this pathname is valid or not. Unless this
            # is the case, this exception implies an ignorable kernel or
            # filesystem complaint (e.g., path not found or inaccessible).
            #
            # Only the following exceptions indicate invalid pathnames:
            #
            # * Instances of the Windows-specific "WindowsError" class
            #   defining the "winerror" attribute whose value is
            #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
            #   fine-grained and hence useful than the generic "errno"
            #   attribute. When a too-long pathname is passed, for example,
            #   "errno" is "ENOENT" (i.e., no such file or directory) rather
            #   than "ENAMETOOLONG" (i.e., file name too long).
            # * Instances of the cross-platform "OSError" class defining the
            #   generic "errno" attribute whose value is either:
            #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
            #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == ERROR_INVALID_NAME:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    # If a "TypeError" exception was raised, it almost certainly has the
    # error message "embedded NUL character" indicating an invalid pathname.
    except TypeError as exc:
        return False
    # If no exception was raised, all path components and hence this
    # pathname itself are valid. (Praise be to the curmudgeonly python.)
    else:
        return True
    # If any other exception was raised, this is an unrelated fatal issue
    # (e.g., a bug). Permit this exception to unwind the call stack.
    #
    # Did we mention this should be shipped with Python already?


if __name__ == '__main__':
    pass
