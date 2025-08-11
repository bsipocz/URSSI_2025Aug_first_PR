from pr_tutorial.simple_functions import factorial,is_prime


def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6


def test_is_prime():
    """Testing is_prime function"""
    assert is_prime(2) # 2 is prime
    assert not is_prime(4) # 4 is composite
    assert not is_prime(1) # 1 is neither prime nor composite
    assert not is_prime(-5) # -5 should probably return an error
    assert is_prime(47) # 47 is prime (and wasn't used in dev)
    try:
        is_prime('uhoh') # handling non-integers?
    except TypeError:
        pass
