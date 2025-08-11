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
	if int_value <=1:
		return False 
	for i in range(2,int(np.sqrt(int_value))+1):
		if int_value % i !=0:
			return False
	return True

