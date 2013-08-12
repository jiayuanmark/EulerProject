
def check(num):
	return sum(map(lambda x : x ** 5, [ int(u) for u in str(num) ])) == num

print sum(filter(lambda x : check(x), range(10, 400000)))