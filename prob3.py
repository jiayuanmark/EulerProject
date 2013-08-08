import math

def prime(num):
	N = int(math.sqrt(num))
	for i in range(2, N+1):
		if num % i == 0:
			return False
	return True

X = 600851475143
L = int(math.sqrt(X))
for i in range(L, 1, -1):
	if prime(i) and X % i == 0:
		print i
		break
