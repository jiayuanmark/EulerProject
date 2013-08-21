

def isValid(a, b, c):
	return (a ** 2) + (b ** 2) == (c ** 2)

def Count(p):
	ret = 0
	for a in xrange(1, p/3):
		for b in xrange(a+1, p/2):
			if (p-a-b) > p/2 or (p-a-b) <= p/6:
				continue
			ret = ret + (1 if isValid(a, b, p-a-b) else 0)
	return ret

table = map(lambda x : Count(x), range(12, 1001))
print sorted(range(12, 1001), key = lambda x : table[x-12], reverse=True)[0] 