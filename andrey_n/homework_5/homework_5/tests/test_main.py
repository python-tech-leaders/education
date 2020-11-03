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
    "input_data,mask,expected",
    [
        (
            "apples, pears # and bananas\ngrapes\nbananas !apples",
            ["#", "!"],
            "apples, pears\ngrapes\nbananas",
        ),
        (
            "apples, pears # and bananas\nbananas ? peach \nbananas ?apples",
            ["#", "?"],
            "apples, pears\nbananas\nbananas",
        ),
    ],
)
def test_strip_comments(input_data, mask, expected):
    """Test strip_comments function"""
    assert main.strip_comments(input_data, mask) == expected


@pytest.mark.parametrize(
    "input_data,mask,expected",
    [
        (
            "apples, pears # and bananas\ngrapes\nbananas !apples",
            ["#", "!"],
            "apples, \ngrapes\nbananas",
        ),
        (
            "apples, pears # and bananas\nbananas ? peach \nbananas ?apples",
            ["#", "?"],
            "apples, pears\nbananas\n",
        ),
    ],
)
def test_strip_comments1(input_data, mask, expected):
    """Test strip_comments function"""
    assert main.strip_comments(input_data, mask) != expected


def test_strip_comments_except():
    """Test strip_comments function raises exception"""
    with pytest.raises(TypeError):
        main.strip_comments(int)


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (62, "1 minute and 2 seconds"),
        (3721, "1 hour, 2 minutes and 1 second"),
    ],
)
def test_format_duration(input_data, expected):
    """Test format_duration function"""
    assert main.format_duration(input_data) == expected


@pytest.mark.parametrize(
    "input_data,expected",
    [(0, "10 sec"), (14, "1 hour, 2 minutes")],
)
def test_format_duration1(input_data, expected):
    """Test format_duration function"""
    assert main.format_duration(input_data) != expected


@pytest.mark.parametrize(
    "input_data,expected",
    [("abb", False), ("Andrey", True)],
)
def test_is_isogram(input_data, expected):
    """Test is_isogram function"""
    assert main.is_isogram(input_data) == expected


@pytest.mark.parametrize(
    "input_data,expected",
    [("daddy", True), ("Dmitro", False)],
)
def test_is_isogram1(input_data, expected):
    """Test is_isogram function"""
    assert main.is_isogram(input_data) != expected


@pytest.mark.parametrize(
    "input_data,expected",
    [
        ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([[1, 2], [3, 4]], [1, 2, 4, 3]),
    ],
)
def test_snail(input_data, expected):
    """Test snail function"""
    assert main.snail(input_data) == expected
