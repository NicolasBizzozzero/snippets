def local_variable_exists(name: str) -> bool:
    """ Return True if the local variable named after 'name' exists, False otherwise.
    """
    return name in locals()


def global_variable_exists(name: str) -> bool:
    """ Return True if the global variable named after 'name' exists, False otherwise.
    """
    return name in globals()


def has_attribute(obj: object, attribute_name: str) -> bool:
    """ Return True if the the object "obj" has an attribute named "attribute_name", False otherwise.
    """
    return hasattr(obj, attribute_name)


if __name__ == '__main__':
    pass
