Ok so I guess you are reading this cuz you wanna use my code. There are some
functions that do stuff and thats:

# API:
## simple_functions
The simple_functions module contains some basic mathematical functions as described below.
All functions can be imported as the following:
    >>> from simple_functions import factorial
    >>> factorial(10)
    9

### factorial

Given an integer, $n$, return the factorial, $n!$. 
Not implemented: negative numbers, floats, arrays
    >>> factorial(0)
    1
    >>> factorial(3)
    6

### fibonacci

Given an number $x$, return the list of numbers in the Fibonnacci
sequence less than $x$.
    >>> fibonnacci(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 

### is_prime

Given an integer $n$, return `True` if $n$ is prime, `False` otherwise.
    >>> isprime(13)
    True
    >>> isprime(2)
    False
    >>> isprime(-1)
    Error: primality is only defined for positive integers

