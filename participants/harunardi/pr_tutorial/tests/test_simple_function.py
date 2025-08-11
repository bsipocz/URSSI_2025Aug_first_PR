from pr_tutorial.simple_functions import factorial
from pr_tutorial.buggy_functions import angle_to_sexigesimal

def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6

def test_angle():
    assert angle_to_sexigesimal(15.72,decimal=3)
