n=int(input())
def number_of_steps(n):
    dp=[[0 for _ in range(10)] for _ in range(n)]
    for i in range(1,10):
        dp[0][i]=1
    for i in range(1, n):
        for num in range(10):
            if num==0:
                dp[i][num]=dp[i-1][1]
            elif num==9:
                dp[i][num]=dp[i-1][8]
            else:
                dp[i][num]=dp[i-1][num-1]+dp[i-1][num+1]
    print(sum(dp[n-1])%1000000000)
number_of_steps(n)
