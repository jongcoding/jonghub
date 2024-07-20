import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1] * (n + 1)


def bfs(r):
    queue = deque([r])
    visited[r] = 0
    cnt = 1
    while queue:
        node = queue.popleft()
        reverse_graph= sorted(graph[node], reverse=True)
        for neighbor in reverse_graph:
            if visited[neighbor] == -1:
                queue.append(neighbor)
                visited[neighbor] = cnt
                cnt += 1

bfs(r)

for i in range(1, n + 1):
    print(visited[i]+1)
