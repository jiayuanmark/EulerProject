from math import factorial
import sys

N, C = 10, 1000000 

lst, free = [], range(0, N)
cnt, digit = 0, 0

while digit < N:
	for i in range(N-digit):
		if cnt + factorial(N-1-digit) > C:
			lst.append(free[i])
			free.remove(lst[-1])
			break
		elif cnt + factorial(N-1-digit) == C:
			lst.append(free[i])
			free.remove(lst[-1])
			free.reverse()
			print "".join([ str(u) for u in (lst + free) ])
			sys.exit(0)
		else:
			cnt = cnt + factorial(N-1-digit)
	digit = digit + 1

print "".join([ str(u) for u in lst ])