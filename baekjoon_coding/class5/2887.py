import sys
input=sys.stdin.readline

def find(parent, x):
    if parent[x] !=x:
        parent[x]=find(parent, parent[x])
    return parent[x]
def union(parent, rank, a, b):
    rootA=find(parent, a)
    rootB=find(parent, b)
    if rank[rootA] > rank[rootB]:
        parent[rootB] = rootA
    elif rank[rootA] < rank[rootB]:
        parent[rootA] = rootB
    else:
        parent[rootB] = rootA
        rank[rootA] += 1 
n=int(input())
planet=[]

for i in range(n):
    x,y,z=map(int, input().split())
    planet.append((x,y,z,i))
edges = []
for d in range(3):
    planet.sort(key=lambda coord: coord[d])
    for i in range(1, n):
        cost = abs(planet[i][d] - planet[i-1][d])
        edges.append((cost, planet[i][3], planet[i-1][3]))
edges.sort()  
parent = list(range(n))
rank = [0] * n
mst_cost = 0
edge_count = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, rank, a, b)
        mst_cost += cost
        edge_count += 1
        if edge_count == n - 1:
            break

print(mst_cost)
