import sys
input=sys.stdin.readline
def max_tri(int_tri, n):
    if n==1:
        return int_tri[0]
    dp=[[0 for _ in range(j+1)] for j in range(n) ]
    dp[0]=int(int_tri[0])
    dp[1]=[int_tri[0]+int_tri[1][0],int_tri[0]+int_tri[1][1]]
    for i in range(2,n):
        for j in range(i+1):
            if j==0:
                dp[i][j]=dp[i-1][0]+int_tri[i][0]
            elif j==i:
                dp[i][j]=dp[i-1][i-1]+int_tri[i][i]
            else:
                dp[i][j]=max(dp[i-1][j]+int_tri[i][j],dp[i-1][j-1]+int_tri[i][j])
    return max(dp[-1])

n=int(input().rstrip())
int_tri=[0]*n
for i in range(n):
    if i==0:
        int_tri[0]=int(input())
    else:
        int_tri[i]=list(map(int, input().split()))
print(max_tri(int_tri,n))
