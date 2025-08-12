from typing import List

def fibonacci(max_value: int) -> List[int]:
    """
    Return the Fibonacci sequence up to a maximum value.

    Parameters
    ----------
    max_value : int
        The maximum value for the Fibonacci sequence.

    Returns
    -------
    List[int]
        The Fibonacci sequence up to `max_value`.
    """
    values = [0, 1]
    while values[-2] + values[-1] < max_value:
        values.append(values[-2] + values[-1])
    return values


def factorial(value: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Parameters
    ----------
    value : int
        A non-negative integer.

    Returns
    -------
    int
        The factorial of `value`.
        
    Raises
    ------
    ValueError
        If `value` is a negative integer.
    """
    if value < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if value == 0:
        return 1
    
    result = 1
    for i in range(1, value + 1):
        result *= i
    return result
