import sys
input = sys.stdin.readline

def min_files(K, files):
    
    prefix_sum = [0] * (K + 1)
    for i in range(1, K + 1):
        prefix_sum[i] = prefix_sum[i - 1] + files[i - 1]

    
    dp = [[0] * K for _ in range(K)]
    knuth = [[0] * K for _ in range(K)]

    for i in range(K - 1):
        dp[i][i + 1] = files[i] + files[i + 1]
        knuth[i][i + 1] = i

 
    for length in range(2, K):
        for i in range(K - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(knuth[i][j - 1], knuth[i + 1][j] + 1):
                cost = dp[i][k] + dp[k + 1][j] + prefix_sum[j + 1] - prefix_sum[i]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    knuth[i][j] = k

    return dp[0][K - 1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        f = list(map(int, input().split()))
        print(min_files(k, f))
