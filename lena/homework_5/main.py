def double_input(input_data):
    """Doubles input"""
    return input_data * 2


def strip_comments(input_string, markers):
    """
    Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
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
    result = input_string.split("\n")
    res_lst = []
    for i in result:
        for j in markers:
            if j in i:
                i = i[: i.index(j)]
                res_lst.append(i)
    return "\n".join(res_lst)


def format_duration(input_seconds):
    """
    Your task is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
    The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

    Examples:

    format_duration(62)    # returns "1 minute and 2 seconds"
    format_duration(3721)  # returns "1 hour, 2 minutes and 1 second"

    Assume that year is 365 days
    """
    if input_seconds == 0:
        return "now"
    if input_seconds < 0:
        return None
    else:
        minutes, seconds = divmod(input_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        years, days = divmod(days, 365)

        def add_s(input_number, text):
            return text + "s" if input_number > 1 else text

        if years:
            return "{} {}, {} {}, {} {}, {} {} and {} {}".format(
                years,
                add_s(years, "year"),
                days,
                add_s(days, "day"),
                hours,
                add_s(hours, "hour"),
                minutes,
                add_s(minutes, "minute"),
                seconds,
                add_s(seconds, "second"),
            )
        elif days:
            return "{} {}, {} {}, {} {} and {} {}".format(
                days,
                add_s(days, "day"),
                hours,
                add_s(hours, "hour"),
                minutes,
                add_s(minutes, "minute"),
                seconds,
                add_s(seconds, "second"),
            )
        elif hours:
            return "{} {}, {} {} and {} {}".format(
                hours,
                add_s(hours, "hour"),
                minutes,
                add_s(minutes, "minute"),
                seconds,
                add_s(seconds, "second"),
            )
        elif minutes > 1:
            return "{} {}, {} {}".format(
                minutes, add_s(minutes, "minute"), seconds, add_s(seconds, "second")
            )
        elif minutes == 1:
            return "{} {} and {} {}".format(
                minutes, add_s(minutes, "minute"), seconds, add_s(seconds, "second")
            )


def is_isogram(input_string):
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
    Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

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
    pass


"""
Lazy init
https://www.codewars.com/kata/59b7b43b4f98a81b2d00000a
"""
