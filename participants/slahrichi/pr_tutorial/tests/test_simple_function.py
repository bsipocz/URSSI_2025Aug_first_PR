from pr_tutorial.simple_functions import factorial
from pr_tutorial.simple_functions import is_prime
from pr_tutorial.buggy_function import angle_to_sexigesimal

def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6


def test_is_prime():
    """Test for prime numbers"""
    
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False

def test_angle_to_sexigesimal():
    """Test the angle_to_sexigesimal function"""
    
    assert angle_to_sexigesimal(180) == '12:00:00.000'
    assert angle_to_sexigesimal(90) == '06:00:00.000'
    assert angle_to_sexigesimal(0) == '00:00:00.000'
    assert angle_to_sexigesimal(360) == '24:00:00.000'
    assert angle_to_sexigesimal(15, decimals=2) == '01:00:00.00'