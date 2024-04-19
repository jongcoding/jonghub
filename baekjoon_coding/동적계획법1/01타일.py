def backtracking(n):
    dp=[0]*(n+1)
    dp[1]=1
    if n>1:
        dp[2]=2
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%15746

    return dp[n]

n = int(input())

print(backtracking(n))