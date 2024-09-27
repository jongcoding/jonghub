N = int(input())
dp = [[[0]*4 for _ in range(10)] for _ in range(100)]
dp[0][0][1] = dp[0][9][2] = 1
print(dp)
for i in range(1, 9):
    dp[0][i][0] = 1
for i in range(N-1):
    for visited in range(4):
        dp[i+1][0][visited|1] += dp[i][1][visited]
        dp[i+1][9][visited|2] += dp[i][8][visited]
        for j in range(1, 9):
            dp[i+1][j][visited] += dp[i][j-1][visited]+dp[i][j+1][visited]
res = 0
for i in range(1, 10):
    res = (res+dp[N-1][i][-1])%1000000000
print(res)