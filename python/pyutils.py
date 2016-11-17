def file_to_string(path_to_file):
    string = ""
    with open(path_to_file, 'r') as file:
        string = file.read()
    return string


def print_file_content(path_to_file):
    with open(path_to_file, 'r') as file:
        line = file.readline()
        while (line != "EOF"):
            print(line, sep="", end="")
            line = file.readline()


def cleanup_string(string_to_cleanup, chars_to_remove_from_the_string):
    new_string = ""

    return new_string


def overwrite_stuff_in_a_file(stuff_to_write, path_to_file):
    with open(path_to_file, 'w') as file:
        file.write(stuff_to_write)


def append_stuff_in_a_file(stuff_to_write, path_to_file):
    with open(path_to_file, 'a') as file:
        file.write(stuff_to_write)


def erase_content_of_a_file(path_to_file):
    with open(path_to_file, 'w') as file:
        file.write("")


def dupe_file(path_to_file, name_of_the_dupe_file):
    content = file_to_string(path_to_file)
    overwrite_stuff_in_a_file(content, name_of_the_dupe_file)


def getline(file: str, line_number: int) -> str:
    """Return the content of file at the line
        indicated by line_number.
    """
    counter = 0
    with open(file, 'r') as file:
        for line in file:
            counter += 1
            if counter == line_number:
                return line
    # If we are here, then the file has a number of lines inferior
    # to line_number
    return ""


if __name__ == '__main__':
    pass
