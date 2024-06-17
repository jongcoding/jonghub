def max_sticker_score(test_cases):
    results = []
    for case in test_cases:
        n, stickers = case
        if n == 1:
            results.append(max(stickers[0][0], stickers[1][0]))
            continue
        
        dp = [[0] * n for _ in range(2)]
        
        dp[0][0] = stickers[0][0]
        dp[1][0] = stickers[1][0]
        
        dp[0][1] = stickers[1][0] + stickers[0][1]
        dp[1][1] = stickers[0][0] + stickers[1][1]
        
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]
        
        results.append(max(dp[0][n-1], dp[1][n-1]))
    
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    test_cases.append((n, [row1, row2]))

results = max_sticker_score(test_cases)


for result in results:
    print(result)
