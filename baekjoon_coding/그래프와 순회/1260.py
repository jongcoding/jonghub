import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
n, m, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS 탐색 결과 저장
dfs_result = []
# BFS 탐색 결과 저장
bfs_result = []

def bfs(start):
    visited = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = 0
    bfs_result.append(start)
    while queue:
        node = queue.popleft()
        graph[node].sort()
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                queue.append(neighbor)
                visited[neighbor] = 1
                bfs_result.append(neighbor)

def dfs(v, visited):
    visited[v] = 1
    dfs_result.append(v)
    for neighbor in sorted(graph[v]):
        if visited[neighbor] == -1:
            dfs(neighbor, visited)

# DFS 탐색
visited = [-1] * (n + 1)
dfs(r, visited)
print(" ".join(map(str, dfs_result)))

# BFS 탐색
bfs(r)
print(" ".join(map(str, bfs_result)))
