from math import sqrt

N = 5000000
table = [ True ] * N
table[0] = False
table[1] = False
table[2] = True

for i in xrange(2, int(sqrt(N))+1):
	if not table[i]:
		continue
	for j in xrange(2, N / i):
		table[i * j] = False

prime = filter(lambda x: table[x], range(1, N))

def factor(num):
	global prime
	temp, ret = num, 0
	for item in prime:
		if item > temp:
			break
		if temp % item == 0:
			ret = ret + 1
		else:
			continue
		while temp % item == 0:
			temp = temp / item
	return ret

begin = 647 
while True:
	found = False
	for x in range(begin, begin+4):
		if factor(x) != 4:
			break
		if x == begin + 3:
			found = True
	if found:
		print begin
		break
	begin = begin + 4


