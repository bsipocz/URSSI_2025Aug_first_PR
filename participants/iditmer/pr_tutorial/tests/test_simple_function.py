from pr_tutorial.simple_functions import factorial
from pr_tutorial.buggy_function import angle_to_sexigesimal


def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6

def test_angle_conversion():
    """Test of specifc value"""

    assert angle_to_sexigesimal(72.3379) == '4:49:21.096'
    assert angle_to_sexigesimal(72.3379, 2) == '4:49:21.10'
    assert angle_to_sexigesimal(72.3379, 1) == '4:49:21.1'