import sys
def number_case(k,coins):
    dp=[0]*(k+1)
    dp[0]=1
    for coin in coins:
        for j in range(coin,k+1):
            dp[j]+=dp[j-coin]
            print(dp)
    return dp[k]
input=sys.stdin.readline
n,k=map(int, input().split())
coins=[int(input()) for _ in range(n)]
print(number_case(k,coins))