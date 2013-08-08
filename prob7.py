from math import sqrt


N = 500000

lst = [True] * N
lst[0] = False
lst[1] = False
lst[2] = True

for i in xrange(2, int(sqrt(N)) + 1):
	if not lst[i]:
		continue
	for j in xrange(i+1, N):
		if lst[j] and j % i == 0:
			lst[j] = False

lst = filter(lambda x : lst[x], range(N))
print lst[10000]