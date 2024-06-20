from collections import deque
import sys
input=sys.stdin.read
def find(n, edges):
    tree =[[] for _ in range(n+1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    parents=[0] * (n+1)

    queue=deque([1]) 
    parents[1]=1

    while queue:
        node =queue.popleft()
        for nei in tree[node]:
            if parents[nei]==0:
                parents[nei] =node
                queue.append(nei)
    return parents

data=input().strip().split()
n=int(data[0])
edges=[((int(data[2*i+1])), int(data[2*i+2])) for i in range(n-1)]

result=find(n,edges)

for i in range(2, n+1):
    print(result[i])