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
    new_strings = ''
    strings = input_string.split('\n')
    for string in strings:
        new_string = string
        for next_symbol in string:
            if next_symbol in markers:
                new_string = string.split(next_symbol)[0]
        new_strings += new_string.strip() + '\n'
    new_strings = new_strings[:-1]  # cut last \n

    print(new_strings)
    return new_strings


def format_duration(input_seconds):
    """
    Your task is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
    The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

    Examples:

    format_duration(62)    # returns "1 minute and 2 seconds"
    format_duration(3721)  # returns "1 hour, 2 minutes and 1 second"

    Assume that year is 365 days
    """
    def check_period(seconds, period):
        quantity = None
        if input_seconds // period > 1:
            quantity = seconds // period
            seconds -= quantity * period
            quantity = str(quantity)
        return quantity, seconds

    if input_seconds == 0:
        return 'now'


    YEAR = 31536000
    DAY = 86400
    HOUR = 3600
    MIN = 60
    # years, days, hours, seconds = None, None, None, None

    # result = datetime.timedelta(seconds=input_seconds)
    # print(result.days, result.minutes, result.seconds)
    seconds = input_seconds

    years, seconds = check_period(seconds, YEAR)
    days, seconds = check_period(seconds, DAY)
    hours, seconds = check_period(seconds, HOUR)
    minutes, seconds = check_period(seconds, MIN)

    result = ''

    if years:
        result += years
        if int(years) > 1:
            result += ' years'
        else:
            result += ' year'
    if days:
        if result != '':
            result += ', '
        result += days
        if int(days) > 1:
            result += ' days'
        else:
            result += ' day'
    if hours:
        if result != '':
            result += ', '
        result += hours
        if int(hours) > 1:
            result += ' hours'
        else:
            result += ' hour'
    if minutes:
        if result != '':
            result += ', '
        result += minutes
        if int(minutes) > 1:
            result += ' minutes'
        else:
            result += ' minute'

    if result != '':
        result += ' and '
    result += str(seconds)
    if int(seconds) > 1:
        result += ' seconds'
    else:
        result += ' second'

    return result


def is_isogram(input_string: str) -> bool:
    """
    An isogram is a word that has no repeating letters, consecutive or non-consecutive.
    Implement a function that determines whether a string that contains only letters is an isogram.
    Assume the empty string is an isogram. Ignore letter case.

    is_isogram("Dermatoglyphics" ) == true
    is_isogram("aba" ) == false
    is_isogram("moOse" ) == false # -- ignore letter case
    """
    all_symbols = list(input_string.lower())
    temp_list = all_symbols
    for symbol in all_symbols:
        temp_list.remove(symbol)
        if symbol in temp_list:
            return False
    return True


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
    result = []
    n = len(input_array[0])
    # for i in range(n):
    #     result.append(input_array[0][i])
    # result.pop()
    # for next_string in input_array:
    #     result.append(next_string[n-1])

    # I can't do this task.

    return result




"""
Lazy init
https://www.codewars.com/kata/59b7b43b4f98a81b2d00000a
"""
if __name__ == '__main__':
    # strip_ex = 'apples, pears # and bananas\ngrapes\nbananas !apples'
    # args = ["#", "!"]
    # strip_comments(strip_ex, args)
    print(format_duration(123456789))
    # format_duration(1)
    # print(is_isogram('oa'))
    pass
    # array = [[1,2,3],
    #          [4,5,6],
    #          [7,8,9]]
    # print(snail(array))
