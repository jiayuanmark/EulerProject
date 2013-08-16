from math import sqrt

N = 1000005
table = [ True ] * N
table[0] = False
table[1] = False
table[2] = True

for i in xrange(2, int(sqrt(N))+1):
	if not table[i]:
		continue
	for j in xrange(2, N/i):
		table[i*j] = False

seq = filter(lambda x : table[x], range(2, 1000000))

max_len, ans = 1, 0

for i in xrange(len(seq)):
	for j in xrange(i+max_len, len(seq)):
		if sum([ seq[u] for u in range(i, j) ]) >= 1000000:
			break 
		if j - i > max_len and table[sum([ seq[u] for u in range(i, j) ])]:
			max_len = j - i
			ans = sum([ seq[u] for u in range(i, j) ])

print ans, max_len
