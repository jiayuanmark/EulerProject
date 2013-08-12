
money = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [ 0 for i in range(205) ] 

dp[0] = 1
for m in money:
	for i in range(m, 201):
		dp[i] = dp[i] + dp[i-m]			

print dp[200]


dp = [ [ 0 for j in range(201) ] for i in range(11) ]

for u in range(1, len(money)+1):
	dp[u][0] = 1


for i in range(1, len(money)+1):
	for j in range(1, 201):
		if j >= money[i-1]:
			dp[i][j] = dp[i-1][j] + dp[i][j-money[i-1]]
		else:
			dp[i][j] = dp[i-1][j]

print dp[len(money)][200]