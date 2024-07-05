import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

def dfs(x, y, m, n, heights, dp):
    if x == m - 1 and y == n - 1:  
        return 1
    if dp[x][y] != -1:  
        return dp[x][y]

    dp[x][y] = 0  

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and heights[x][y] > heights[nx][ny]:
            dp[x][y] += dfs(nx, ny, m, n, heights, dp)
    
    return dp[x][y]

def find_paths(m, n, heights):
    dp = [[-1] * n for _ in range(m)]
    return dfs(0, 0, m, n, heights, dp)


data = input().split()
m = int(data[0])
n = int(data[1])
heights = []
index = 2
for i in range(m):
    heights.append(list(map(int, data[index:index + n])))
    index += n


print(find_paths(m, n, heights))
