

ans, N = 1, 1001
level = range(1, N+1, 2)
for idx in range(1, len(level)):
	content = range(level[idx-1]*level[idx-1]+1, level[idx] * level[idx] + 1)
	ans = ans + sum([ content[u] for u in range(2 * idx-1, len(content),  2*idx) ])
print ans