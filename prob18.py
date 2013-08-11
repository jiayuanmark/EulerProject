
triangle = []

f = file('input_18', 'r')
lines = f.readlines()
for item in lines:
	triangle.append([ int(u) for u in item.strip().split() ])

N = len(triangle)
dp = [ [ 0 for j in range(i+1)] for i in range(N) ]

dp[0][0] = triangle[0][0]

for l in range(1, N):
	for i in range(l+1):
		if i == 0:
			dp[l][i] = triangle[l][i] + dp[l-1][i]
		elif i == l:
			dp[l][i] = triangle[l][i] + dp[l-1][i-1]
		else:
			dp[l][i] = triangle[l][i] + max(dp[l-1][i], dp[l-1][i-1])

print max(dp[N-1])

