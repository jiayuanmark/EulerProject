from math import sqrt


N = 2000000

lst = [True] * N
lst[0] = False
lst[1] = False
lst[2] = True

for i in xrange(2, int(sqrt(N)) + 1):
	if not lst[i]:
		continue
	for j in xrange(i*i, N, i):
		lst[j] = False

print sum(filter(lambda x : lst[x], range(N))) 