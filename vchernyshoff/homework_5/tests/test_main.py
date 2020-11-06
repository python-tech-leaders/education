import pytest

import main


# double_input ====================================================================================
@pytest.mark.parametrize(
    "input_data,expected",
    [
        (10, 20),
        ([1, 2], [1, 2, 1, 2])
    ],
)
def test_double_input(input_data, expected):
    """Test double_input function"""
    assert main.double_input(input_data) == expected


def test_double_input_raises():
    """Test double_input function raises exception"""
    with pytest.raises(TypeError):
        main.double_input(list)


# strip_comments ====================================================================================
@pytest.mark.parametrize(
    "input_string, input_separators, expected",
    [
        (
                'apples, pears # and bananas\ngrapes\nbananas !apples',
                ["#", "!"],
                'apples, pears\ngrapes\nbananas'
        )
    ],
)
def test_strip_comments(input_string, input_separators, expected):
    """Test strip_comments function"""
    assert main.strip_comments(input_string, input_separators) == expected


# format_duration ====================================================================================
@pytest.mark.parametrize(
    "input_seconds, expected",
    [
        (1, '1 second'),
        (123456789, '3 years, 333 days, 21 hours, 33 minutes and 9 seconds'),
        (0, 'now')
    ],
)
def test_format_duration(input_seconds, expected):
    """Test format_duration function"""
    assert main.format_duration(input_seconds) == expected


def test_format_duration_raises():
    """Test double_input function raises exception"""
    with pytest.raises(TypeError):
        main.format_duration(str, list, dict, set)


# is_isogram ====================================================================================
@pytest.mark.parametrize(
    "input_data,expected",
    [
        ('abcde', True),
        ('abcdAe', False),
        ('aabcde', False),
    ],
)
def test_is_isogram(input_data, expected):
    """Test is_isogram function"""
    assert main.is_isogram(input_data) == expected


# is_isogram ====================================================================================
@pytest.mark.parametrize(
    "input_data,expected",
    [
        ([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 3],
          [2, 4]], [1, 3, 4, 2]),

    ],
)
def test_snail(input_data, expected):
    """Test is_isogram function"""
    pass
