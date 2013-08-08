
def diff(N):
	return N * N * (N+1) * (N+1) / 4 - (N+1) * (2 * N + 1) * N / 6

print diff(10)
print diff(100)