n=int(input())
costs=[list(map(int, input().split())) for _ in range(n)]
dp=[[0 for _ in range(3)] for _ in range(n)]

for i in range(3):
    dp[0][i]=costs[0][i]
for i in range(1, n):
    dp[i][0]=costs[i][0]+min(dp[i-1][1],dp[i-1][2])
    dp[i][1]=costs[i][1]+min(dp[i-1][0],dp[i-1][2])
    dp[i][2]=costs[i][2]+min(dp[i-1][0], dp[i-1][1])
min_cost=min(dp[n-1])
print(min_cost)