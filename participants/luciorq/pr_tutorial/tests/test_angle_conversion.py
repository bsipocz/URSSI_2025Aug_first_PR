import pytest
from pr_tutorial.buggy_function import angle_to_sexagesimal


@pytest.mark.parametrize(
    "angle, decimals, expected",
    [
        (180, 3, "12:0:0.000"),
        (90, 0, "6:0:0"),
        (45, 5, "3:0:0.00000"),
        (23.456, 2, "1:33:49.44"),
    ],
)
def test_angle_to_sexagesimal(angle, decimals, expected):
    """Test the angle_to_sexagesimal function with various angles and decimal places."""
    assert angle_to_sexagesimal(angle, decimals=decimals) == expected


def test_angle_to_sexagesimal_invalid_decimals():
    """Test that angle_to_sexagesimal raises a ValueError for non-integer decimals."""
    with pytest.raises(ValueError):
        angle_to_sexagesimal(90, decimals=1.5)


def test_angle_to_sexagesimal_invalid_angle():
    """Test that angle_to_sexagesimal raises a ValueError for out-of-range angles."""
    with pytest.raises(ValueError):
        angle_to_sexagesimal(-10)
    with pytest.raises(ValueError):
        angle_to_sexagesimal(400)
