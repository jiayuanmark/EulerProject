from math import sqrt

def abundant(num):
	if num < 12:
		return False
	else:
		ret = 1 + sum(map(lambda x : (x + num/x if num % x == 0 else 0), range(2, int(sqrt(num))+1)))
		ret = ret - (int(sqrt(num)) if num % sqrt(num) == 0 else 0)
		return ret > num

def decomposable(num):
	global table
	if num < 24:
		return False
	for i in xrange(12, num/2+1):
		if i in table and num-i in table:
			return True
	return False

table = set(filter(lambda x : abundant(x) == True, range(1, 28123)))
print sum(filter(lambda x : decomposable(x) == False, range(1, 28124)))
