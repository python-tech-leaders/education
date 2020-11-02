import pytest

# import vchernyshoff.homework_5.main as main
import main

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




@pytest.mark.parametrize(
    "input_seconds, expected",
    [
        (1,'1 seconds'),
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

# def test_double_input_raises():
#     """Test double_input function raises exception"""
#     with pytest.raises(TypeError):
#         main.double_input(list)
