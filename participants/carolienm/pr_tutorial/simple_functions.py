def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values

def is_prime(number):
    if number < 2:
        prime = False
    else:
        hi_number = int(number ** 0.5 + 1)
        prime = all(number % i for i in range(2, hi_number))
    return prime

def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)
