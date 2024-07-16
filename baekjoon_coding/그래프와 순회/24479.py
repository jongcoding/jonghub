import sys
input=sys.stdin.readline
# 정확히는 파이썬 스택, 함수 콜스택의 깊이 한계
sys.setrecursionlimit(10**5)
N,M,R=map(int, input().rstrip().split())
visited=[0]*(N+1)
graph=[[] for _ in range(N+1)]
cnt=0
def dfs(v):
    global cnt
    sort_graph=sorted(graph[v])
    cnt+=1
    visited[v]=cnt

    for i in sort_graph:
        if visited[i]==0:
            dfs(i)
            

for i in range(M):
    u,v=map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

dfs(R)

for i in range(1, N+1):
    print(visited[i])