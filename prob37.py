from math import sqrt

def prime(num):
	if num == 1:
		return False
	for i in xrange(2, int(sqrt(num))+1):
		if num % i == 0:
			return False
	return True

def valid(num):
	s = str(num)
	for i in range(1, len(s)+1):
		if not prime(int(s[0:i])):
			return False
	return True



ans = []
cndd = [2, 3, 5, 7]
level = 1

while len(ans) < 11:
	app = filter(lambda x: x < (10 ** level), cndd)
	for item in app:
		for i in range(1, 10):
			num = i * (10 ** level) + item
			if prime(num):
				cndd.append(num)
			if valid(num):
				ans.append(num)
	level = level + 1
print sum(ans)


