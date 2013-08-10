from math import sqrt


def check(num):
	ret = 0
	for i in xrange(1, int(sqrt(num)) + 1):
		if num % i == 0:
			ret += 2
	return ret


for i in xrange(100000):
	num = (i + 1) * i / 2
	if check(num) > 500:
		print num
		break
