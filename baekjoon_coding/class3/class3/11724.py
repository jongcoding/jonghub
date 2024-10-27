import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(node):
    visited[node] = True
    for neighbor in stack[node]:
        if not visited[neighbor]:
            dfs(neighbor)
n,m=map(int, input().split())
stack=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int, input().split())
    stack[u].append(v)
    stack[v].append(u)
visited=[False]*(n+1)
connected=0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        connected+=1
print(connected)