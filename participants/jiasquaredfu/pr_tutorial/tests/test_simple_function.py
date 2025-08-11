from pr_tutorial.simple_functions import factorial, is_prime


def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6

def test_prime():
	assert is_prime(3) == True
