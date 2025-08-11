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

def isprime(n):
    if n < 2:
        return False
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    else:
        return True
