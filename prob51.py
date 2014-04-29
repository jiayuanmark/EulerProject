from math import sqrt
import sys

def isPrime (x):
	if x <= 1:
		return False		  
	for div in xrange(2, int(sqrt(x))):
		if x % div == 0:
			return False
	return True


def minDigits (num):
	return min (str(num))


def replaceNum (num, old, new):
	if old not in str(num):
		return 0
	elif str(num).startswith(old) and new == '0':
		return 0
	else:
		return int(''.join(map(lambda x : new if x == old else x, str(num))))


if __name__ == "__main__":
	num = 56004
	digs = set(['0', '1', '2'])
	char = '0123456789'

	while True:
		if isPrime (num) and minDigits (num) in digs:
			for dig in range(int(minDigits(num)), 9):
				temp = filter (lambda x : isPrime(x), map (lambda x : replaceNum(num, str(dig), x), char) )
				if len (temp) == 8: 
					print num
					print temp
					sys.exit (0)
		num += 1

