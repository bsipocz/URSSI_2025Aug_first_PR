from pr_tutorial.simple_functions import factorial
from pr_tutorial.simple_functions import is_prime


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