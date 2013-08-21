import sys
from math import sqrt
from itertools import permutations

def Sieve(N):
	table = [ True ] * N
	table[0] = table[1] = False

	for i in xrange(2, int(sqrt(N))+1):
		if not table[i]:
			continue
		for j in range(2, N / i):
			table[i * j] = False
	
	return filter(lambda x : table[x], range(N))

def IsPandigit(num):
	if len(str(num)) != len(set(str(num))):
		return False
	for u in str(num):
		if u == '0' or int(u) > len(str(num)):
			return False
	return True

def IsPrime(num):
	for i in xrange(2, int(sqrt(num))+1):
		if num % i == 0:
			return False
	return True

if __name__ == "__main__":
	S, L = '987654321', 9
	while L >= 1:
		for item in permutations(S[-L:], L):
			num = int("".join(item))
			if IsPrime(num):
				print num
				sys.exit(0)
		L = L - 1