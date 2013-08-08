
def sieve(N):
	lst = range(1, N+1)
	for i in range(len(lst)):
		for j in range(i+1, len(lst)):
			if lst[j] % lst[i] == 0:
				lst[j] = lst[j] / lst[i]
	return lst

print reduce(lambda x, y : x * y, sieve(20))

