
table = {}

def check(num):
	global table
	if num in table:
		return table[num]
	elif num % 2 == 0:
		table[num] =  1 + check(num / 2)
		return table[num]
	else:
		table[num] = 1 + check(3 * num + 1)
		return table[num]

table[1] = 1
result = map(lambda x : check(x), range(1, 1000000))
print sorted(range(1, 1000000), key=lambda x : result[x-1], reverse=True)[0]
