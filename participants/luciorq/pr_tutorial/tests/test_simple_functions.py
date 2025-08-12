import pytest
from pr_tutorial.simple_functions import factorial, fibonacci


@pytest.mark.parametrize(
    "value, expected",
    [
        (0, 1),
        (1, 1),
        (3, 6),
        (5, 120),
    ],
)
def test_factorial(value, expected):
    """Test the factorial function with various values."""
    assert factorial(value) == expected


def test_factorial_negative():
    """Test that the factorial function raises a ValueError for negative input."""
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize(
    "max_value, expected",
    [
        (2, [0, 1, 1]),
        (10, [0, 1, 1, 2, 3, 5, 8]),
        (1, [0, 1]),
    ],
)
def test_fibonacci(max_value, expected):
    """Test the fibonacci function with various maximum values."""
    assert fibonacci(max_value) == expected
