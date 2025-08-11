import numpy as np 
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


def is_prime(int_value):
	for i in range(0,int(np.sqrt(int_value))):
		if int_value/i !=0:
			return False
		else:
			return True

