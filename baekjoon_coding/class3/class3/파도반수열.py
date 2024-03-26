def side_length(n):
    dp=[0]*(101)
    dp[1]=1
    dp[2]=1
    dp[3]=1
    if n==1:
        return dp[1]
    elif n==2:
        return dp[2]
    elif n==3:
        return dp[3]
    else:
        for i in range(4, n+1):
            dp[i]=dp[i-3]+dp[i-2]
        return dp[n]
t=int(input())
for _ in range(t):
    n=int(input())
    print(side_length(n))