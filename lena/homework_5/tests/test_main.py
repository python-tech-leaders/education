import pytest

import main


@pytest.mark.parametrize(
    "input_data,expected",
    [(10, 20), ([1, 2], [1, 2, 1, 2])],
)
def test_double_input(input_data, expected):
    """Test double_input function"""
    assert main.double_input(input_data) == expected


def test_double_input_raises():
    """Test double_input function raises exception"""
    with pytest.raises(TypeError):
        main.double_input(list)


@pytest.mark.parametrize(
    "input_data,expected",
    [("", True), ("Mother", True), ("mum", False), ("Test", False)],
)
def test_is_isogram(input_data, expected):
    """Test is_isogram function"""
    assert main.is_isogram(input_data) == expected


def test_is_isogram_raises():
    """Test double_input function raises exception"""
    with pytest.raises(AttributeError):
        main.is_isogram(1)


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (-1, None),
        (0, "now"),
        (62, "1 minute and 2 seconds"),
        (3721, "1 hour, 2 minutes and 1 second"),
        (103721, "1 day, 4 hours, 48 minutes and 41 seconds"),
        (3333721, "38 days, 14 hours, 2 minutes and 1 second"),
        (33333721, "1 year, 20 days, 19 hours, 22 minutes and 1 second"),
    ],
)
def test_format_duration(input_data, expected):
    """Test format_duration function"""
    assert main.format_duration(input_data) == expected


def test_negative_format_duration(input_data=-1, expected="-1 second"):
    """Test format_duration function with negative argument"""
    assert main.format_duration(input_data) != expected


@pytest.mark.parametrize(
    "input_string,input_separators,expected",
    [
        (
            "apples, pears # and bananas\ngrapes\nbananas !apples",
            ["#", "!"],
            "apples, pears\ngrapes\nbananas",
        ),
        (
            "  apples, pears # and bla-bla\ngrapes ?hello\nbananas !apples.  ",
            ["#", "!", "?"],
            "apples, pears\ngrapes\nbananas",
        ),
    ],
)
def test_strip_comments(input_string, input_separators, expected):
    """Test strip_comments function"""
    assert main.strip_comments(input_string, input_separators) == expected
