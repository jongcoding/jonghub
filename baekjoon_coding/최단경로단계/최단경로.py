import heapq
import sys
input=sys.stdin.readline
INF = int(1e9)
def dijkstra(v, start, graph):
    dis=[INF]*(v+1)
    dis[start]=0
    queue=[]
    heapq.heappush(queue,(0,start))

    while queue:
        cur_dis,cur_node=heapq.heappop(queue)
        if cur_dis >dis[cur_node]:
            continue
        for adj, wei in graph[cur_node]:
            path=cur_dis+wei
            if path< dis[adj]:
                dis[adj]=path
                heapq.heappush(queue, (path, adj))
    return dis
v,e=map(int ,input().split())
k=int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, to, w = map(int, input().split())
    graph[u].append((to,w))

dis=dijkstra(v,k,graph)
for i in range(1,v+1):
    if dis[i]==INF:
        print("INF")
    else:
        print(dis[i])
