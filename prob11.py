 
matrix = []

f = file('input_11', 'r')
lines = f.readlines()
for item in lines:
	matrix.append( [ int(u) for u in item.strip().split() ] )

assert(len(matrix) == 20 and len(matrix[0]) == 20)

ans = 0
for i in xrange(20):
	for j in xrange(20):
		if j < 17:
			ans = max(ans, reduce(lambda x, y : x * y, [ matrix[i][j+u] for u in range(4) ]))
		if i < 17:
			ans = max(ans, reduce(lambda x, y : x * y, [ matrix[i+u][j] for u in range(4) ]))
		if i < 17 and j < 17:
			ans = max(ans, reduce(lambda x, y : x * y, [ matrix[i+u][j+u] for u in range(4) ]))
		if i < 17 and j >= 3:
			ans = max(ans, reduce(lambda x, y : x * y, [ matrix[i+u][j-u] for u in range(4) ]))
		if i >= 3 and j < 17:
			ans = max(ans, reduce(lambda x, y : x * y, [ matrix[i-u][j+u] for u in range(4) ]))
print ans

