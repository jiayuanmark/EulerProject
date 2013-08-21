import sys

N = 10000
table = [ u * (3*u-1) / 2 for u in range(1, N) ]
S = set(table)

'''
for first in table:
	for second in table:
		if first == second:
			continue
		if first + second in S and abs(first - second) in S:
			print abs(first - second)
			sys.exit(0)
'''

for diff in table:
	for first in table:
		if first + diff > table[-1]:
			continue
		if first + diff in S and 2 * first + diff in S:
			print diff
			sys.exit(0)