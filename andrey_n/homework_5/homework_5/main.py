def double_input(input_data):
    """Doubles input"""
    return input_data * 2


def clean(item: str, markers: list) -> str:
    """Delete comments from item"""
    for mark in markers:
        if mark in item:
            return item[: item.index(mark)]
    return item


def strip_comments(input_string: str, markers: list) -> str:
    """
    Complete the solution so that it strips all text that follows any of a set of
    comment markers passed in.
    Any whitespace at the end of the line should also be stripped out.

    Example:

    Input string:

    "
    apples, pears # and bananas
    grapes
    bananas !apples
    "

    Markers: ["#", "!"]

    The output expected would be:

    "
    apples, pears
    grapes
    bananas
    "

    result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    # "apples, pears\ngrapes\nbananas"
    """
    _str = input_string.split("\n")
    res = []
    for item in _str:
        res.append(clean(item, markers).strip())
    return "\n".join(res)


def format_duration(input_seconds: int) -> str:
    """
    Your task is to write a function which formats a duration, given as
    a number of seconds, in a human-friendly way.
    The function must accept a non-negative integer. If it is zero, it just returns "now".
    Otherwise, the duration is expressed as a combination of years, days, hours,
    minutes and seconds.

    Examples:

    format_duration(62)    # returns "1 minute and 2 seconds"
    format_duration(3721)  # returns "1 hour, 2 minutes and 1 second"

    Assume that year is 365 days
    """
    res = []
    if input_seconds == 0:
        return "now"
    minutes, seconds = divmod(input_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)
    all_date = [
        (years, "year"),
        (days, "day"),
        (hours, "hour"),
        (minutes, "minute"),
        (seconds, "second"),
    ]
    real_date = [item for item in all_date if item[0]]
    for item in real_date:
        if item[0] > 1:
            res.append(f"{item[0]} {item[1]}s")
        else:
            res.append(f"{item[0]} {item[1]}")
    last = " and " + res.pop()
    return ", ".join(res) + last


def is_isogram(input_string: str) -> bool:
    """
    An isogram is a word that has no repeating letters, consecutive or non-consecutive.
    Implement a function that determines whether a string that contains only letters is an isogram.
    Assume the empty string is an isogram. Ignore letter case.

    is_isogram("Dermatoglyphics" ) == true
    is_isogram("aba" ) == false
    is_isogram("moOse" ) == false # -- ignore letter case
    """
    return len(set(input_string.lower())) == len(input_string)


def snail(input_array):
    """
    Given an n x n array, return the array elements arranged from outermost elements to the
    middle element, traveling clockwise.

    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    snail(array) #=> [1,2,3,6,9,8,7,4,5]
    For better understanding, please follow the numbers of the next array consecutively:

    array = [[1,2,3],
             [8,9,4],
             [7,6,5]]
    snail(array) #=> [1,2,3,4,5,6,7,8,9]

    For better understanding: http://www.haan.lu/files/2513/8347/2456/snail.png
    """
    res = []
    if not input_array:
        return res
    row_start = 0
    col_start = 0
    row_end = len(input_array) - 1
    col_end = len(input_array) - 1

    while len(res) != (len(input_array) * len(input_array[0])):

        for i in range(col_start, col_end + 1):
            res.append(input_array[row_start][i])
        row_start += 1

        for i in range(row_start, row_end + 1):
            res.append(input_array[i][col_end])
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                res.append(input_array[row_end][i])
        row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                res.append(input_array[i][col_start])
        col_start += 1

    return res
