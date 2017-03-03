from time import localtime


def get_day_of_week() -> int:
    """ Return the day of today with 0 corresponding to monday and 6 to
        sunday.
    """
    return localtime()[6]


if __name__ == '__main__':
    pass
