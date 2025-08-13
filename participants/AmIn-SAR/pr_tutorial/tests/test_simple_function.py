from pr_tutorial.simple_functions import factorial
from pr_tutorial.buggy_function import angle_to_sexigesimal

def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6

def test_ang2sexig():
    print(angle_to_sexigesimal(31.2))

 