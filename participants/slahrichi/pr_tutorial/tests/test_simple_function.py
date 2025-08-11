from pr_tutorial.simple_functions import factorial
from pr_tutorial.buggy_function import angle_to_sexigesimal

def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6


def test_angle_to_sexigesimal():
    """Test the angle_to_sexigesimal function"""
    
    assert angle_to_sexigesimal(180) == '12:00:00.000'
    assert angle_to_sexigesimal(90) == '06:00:00.000'
    assert angle_to_sexigesimal(0) == '00:00:00.000'
    assert angle_to_sexigesimal(360) == '24:00:00.000'
    assert angle_to_sexigesimal(15, decimals=2) == '01:00:00.00'