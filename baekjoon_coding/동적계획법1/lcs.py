def LCS(a, b):
    
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1  # 문자가 일치하는 경우
             
            else:
               
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 문자가 일치하지 않는 경우 최댓값 선택

    return dp[-1][-1]

a = input().strip()
b = input().strip()
print(LCS(a, b))
