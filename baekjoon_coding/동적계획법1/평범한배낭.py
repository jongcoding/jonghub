import sys
input = sys.stdin.readline

def best_benefit(w, v, k):
    dp = [0] * (k + 1)  # 최대 무게 k까지 고려하는 DP 배열
    for i in range(len(w)):
        for j in range(k, w[i] - 1, -1):  # 무게가 k부터 w[i]까지 역순으로 갱신
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])  # 현재 아이템을 포함할 경우와 포함하지 않을 경우 중 더 큰 값으로 갱신
    return max(dp)

n, k = map(int, input().rstrip().split())
w, v = [], []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    w.append(a)
    v.append(b)

print(best_benefit(w, v, k))
