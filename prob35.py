from math import sqrt

def prime(num):
	for i in range(2, int(sqrt(num))+1):
		if num % i == 0:
			return False
	return True

def cycle_prime(num):
	s = str(num)
	ss = s + s
	for i in range(len(s)):
		if not prime(int(ss[i:i+len(s)])):
			return False
	return True

print sum(map(lambda x : 1 if cycle_prime(x) else 0, range(2, 1000000)))