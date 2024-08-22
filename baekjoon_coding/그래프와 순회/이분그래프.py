from collections import deque
import sys
input = sys.stdin.readline
K = int(input().rstrip())

def is_bipartite(V, adj_list):
    colors = [-1] * (V + 1)

    for start in range(1, V + 1):
        if colors[start] == -1:  
            queue = deque([start])
            colors[start] = 0 
            
            while queue:
                node = queue.popleft()
                current_color = colors[node]
                
                for neighbor in adj_list[node]:
                    if colors[neighbor] == -1:
                       
                        colors[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif colors[neighbor] == current_color:
    
                        return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    if is_bipartite(V, adj_list):
        print("YES")
    else:
        print("NO")
