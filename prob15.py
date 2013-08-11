
dp = [ [0 for j in xrange(50)] for i in xrange(50) ]

for i in xrange(0, 41):
	dp[i][0] = 1

for i in xrange(1, 41):
	for j in xrange(1, 21):
		dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


print dp[4][2]
print dp[40][20]