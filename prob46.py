from math import sqrt

N = 50000
table = [ True ] * N
table[0] = False
table[1] = False
table[2] = True

for i in xrange(2, int(sqrt(N))+1):
	if not table[i]:
		continue
	for j in xrange(2, N / i):
		table[i * j] = False

prime = filter(lambda x: table[x], range(1, N))

def check(num, ele):
	if (num - ele) % 2 != 0:
		return False
	temp = (num - ele) / 2
	return int(sqrt(temp)) ** 2 == temp


def decomposable(num):
	for item in prime:
		if item >= num:
			break
		if check(num, item):
			return True
	return False

print min(filter(lambda x : x not in prime and not decomposable(x), range(13, 6000, 2)))