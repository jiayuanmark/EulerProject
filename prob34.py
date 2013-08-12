from math import factorial

def check(num):
	return sum(map(lambda x:factorial(int(x)), str(num))) == num

print sum(filter(lambda x:check(x), range(11, 2000000)))