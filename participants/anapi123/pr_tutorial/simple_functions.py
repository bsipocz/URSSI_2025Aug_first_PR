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
    
# Add a new function in simple_functions.py called is_prime that takes an integer number and returns True if the number is prime, and False if not.
def is_prime(num: int) -> bool:
    if num % 2 != 1:
        return True
    else:
        return False
