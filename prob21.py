from math import sqrt

def sum_divisor(num):
	if num == 1:
		return 0
	else:
		ret = 1 + sum(map(lambda x : (x + num/x if num % x == 0 else 0), range(2, int(sqrt(num))+1)))
		ret = ret - (int(sqrt(num)) if num % sqrt(num) == 0 else 0) 
		return ret

ans = 0
for i in xrange(2, 10001):
	if sum_divisor(sum_divisor(i)) == i and i != sum_divisor(i):
		ans = ans + i

print ans

		
