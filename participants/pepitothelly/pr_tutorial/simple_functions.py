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

def is_prime(number):
    if number <= 1:
        return False
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

num = int(input("Type in a number: "))
print(is_prime(num))
