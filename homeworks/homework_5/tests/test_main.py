import pytest

import main


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
