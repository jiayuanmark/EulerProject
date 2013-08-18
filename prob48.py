

def pow_with_mod(num, pow, mod):
	ret = 1
	for i in xrange(pow):
		ret = (ret * num) % mod
	return ret

def sum_with_mod(lst, mod):
	ret = 0
	for item in lst:
		ret = (ret + item) % mod
	return ret

print sum_with_mod(map(lambda x : pow_with_mod(x, x, 10000000000), range(1, 1001)), 10000000000)

