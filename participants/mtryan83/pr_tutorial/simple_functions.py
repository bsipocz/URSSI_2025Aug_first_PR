from math import ceil,sqrt

def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

def is_prime(n: int) -> bool:
    """
    Return whether the input positive integer is prime
    Parameter:
        n - Positive integer
    Returns:
        True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    nrt = sqrt(n)
    # check if n is a square number
    if nrt==ceil(nrt):
        return False
    # otherwise check if any factors less than sqrt(n)+1
    for x in range(2,ceil(nrt)):
        if not n%x:
            return False
    return True
