def cal(matirx):
    n=len(matrix)
    dp=[[0] *n for _ in range(n)]

    for lenght in range(2,n):
        for i in range(1, n-lenght+1):
            j=i+lenght-1
            dp[i][j]=float('inf')
            for k in range(i,j):
                q=dp[i][k]+dp[k+1][j]+matirx[i-1]*matirx[k]*matrix[j]
                if q <dp[i][j]:
                    dp[i][j]=q
    return dp[1][n-1]
n=int(input())
matrix=[]
for _ in range(n):
    r,c=map(int, input().split())
    matrix.append(r)
matrix.append(c)
print(cal(matrix))