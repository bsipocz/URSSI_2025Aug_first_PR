
def fibonacci(min_value):
    a, b = 0, 1
    while b < min_value:
        a, b = b, a + b
    return b

