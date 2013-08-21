
def is_legal(num):
	if '0' in str(num):
		return False
	return True

def is_unique(L, num):
	return len(L + str(num)) == len(set(L + str(num)))

def pandigital_multiple(num):
	if len(str(num)) >= 9:
		return False
	L, n = "", 1
	while len(L) < 9:
		temp = num * n
		if not is_legal(temp) or not is_unique(L, temp):
			return False
		L = L + str(temp)
		n = n + 1
	return L if len(L) == 9 else False

val = filter(lambda x : x, map(lambda x : pandigital_multiple(x), range(1, 10000)))
print max(map(lambda x : int(x), val))


