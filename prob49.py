from math import sqrt
import sys

def perm_check(num1, num2):
	return ''.join(sorted([ u for u in str(num1)])) == ''.join(sorted([ u for u in str(num2)]))

N = 20000
table = [ True ] * N
table[0] = False
table[1] = False
table[2] = True

for i in xrange(2, int(sqrt(N))+1):
	if not table[i]:
		continue
	for j in xrange(2, N/i):
		table[i*j] = False

seq = filter(lambda x : table[x], range(1001, 10000))

ans = []

for i in xrange(len(seq)):
	for j in xrange(i + 1, len(seq)):
		if 2 * seq[j] - seq[i] >= 10000:
			break 
		if perm_check(seq[i], seq[j]) and table[2 * seq[j] - seq[i]] and perm_check(seq[j], 2 * seq[j] - seq[i]):
			ans.append((seq[i], seq[j], 2 * seq[j] - seq[i]))
			if len(ans) == 2:
				for u in ans:
					print ''.join([ str(v) for v in u ])
				sys.exit(0)