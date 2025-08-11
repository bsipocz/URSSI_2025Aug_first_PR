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

import math
def is_prime(num):
    if num <= 1:
        return False   
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

