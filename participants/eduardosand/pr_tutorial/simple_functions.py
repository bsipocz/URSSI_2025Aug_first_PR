def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    """
    Return the factorial of a function. Has to be an integer.
    :param value: (float)
    :return: factorial of the value
    """
    assert type(value) == int
    if value == 0:
        return 1
    else:
        running_value = 1
        for i in range(int(value)):
            running_value *= value-i
        return running_value
