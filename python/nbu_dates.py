import time
import datetime


FORMAT_YEAR_WITHOUT_CENTURY = "%y"    # 00, 01, …, 99
FORMAT_FULL_YEAR = "%Y"               # 0001, …, 2013, 2014, …, 9998, 9999
FORMAT_FULL_YEAR_ISO_8601 = "%G"      # 0001, …, 2013, 2014, …, 9998, 9999

FORMAT_YEARDAY = "%j"                 # 001, 002, …, 366

FORMAT_ABBREVIATED_MONTH = "%b"       # Jan, Feb, …, Dec
FORMAT_FULL_MONTH = "%B"              # January, February, …, December
FORMAT_INDEX_MONTH = "%m"             # 01, 02, …, 12

FORMAT_YEARWEEK_FIRST_SUNDAY = "%U"   # 00, 01, …, 53
FORMAT_YEARWEEK_FIRST_MONDAY = "%W"   # 00, 01, …, 53
FORMAT_YEARWEEK_ISO_8601 = "%V"       # 01, 02, …, 53

FORMAT_ABBREVIATED_WEEKDAY = "%a"     # Sun, Mon, …, Sat
FORMAT_FULL_WEEKDAY = "%A"            # Sunday, Monday, …, Saturday
FORMAT_INDEX_WEEKDAY = "%w"           # 0, 1, …, 6
FORMAT_INDEX_WEEKDAY_ISO_8601 = "%u"  # 1, 2, …, 7

FORMAT_DAY = "%d"                     # 01, 02, …, 31

FORMAT_HOUR_24 = "%H"                 # 00, 01, …, 23
FORMAT_HOUR_12 = "%I"                 # 01, 02, …, 12
FORMAT_AM_PM = "%p"                   # AM, PM

FORMAT_MINUTES = "%M"                 # 00, 01, …, 59

FORMAT_SECONDS = "%S"                 # 00, 01, …, 59

FORMAT_MICROSECONDS = "%f"            # 000000, 000001, …, 999999

FORMAT_UTC_OFFSET = "%z"              # (empty), +0000, -0400, +1030
FORMAT_TIME_ZONE_NAME = "%Z"          # (empty), UTC, EST, CST
FORMAT_LOCAL_DATE_TIME = "%c"         # Tue Aug 16 21:30:00 1988
FORMAT_LOCAL_DATE = "%x"              # 08/16/1988
FORMAT_LOCAL_TIME = "%X"              # 21:30:00


def get_day_of_week() -> int:
    """ Return the day of today with 0 corresponding to monday and 6 to
        sunday.
    """
    return time.localtime()[6]


def str_to_date(string: str, parse_format: str) -> datetime.datetime:
    return datetime.strptime(string, parse_format)


if __name__ == '__main__':
    pass
