from itertools import permutations

def check(s):
	num1, num2, num3 = int(s[0:2]), int(s[2:5]), int(s[5:])
	if num1 * num2 == num3:
		return True
	num1, num2, num3 = int(s[0]), int(s[1:5]), int(s[5:])
	if num1 * num2 == num3:
		return True
	return False

print sum( set(map(lambda x : int(x[5:]) if check(x) else 0, [ ''.join(u) for u in permutations('123456789', 9)] )) )
