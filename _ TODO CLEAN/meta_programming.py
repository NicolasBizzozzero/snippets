def get_extracting_class(attributes: List[str], default_type: str = "str") -> str:
    result = "def __init__(" + (": " + default_type +
                                " = None, ").join(attributes) + ": str = None):\n"

    for a in attributes:
        result += "\tself." + a + " = " + a + "\n"

    return result
