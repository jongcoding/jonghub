from collections import deque
def bfs(n,k):
    max=100000
    visited=[False]*(max+1)

    queue=deque([(n,0)])
    visited[n]=True
    while queue:
        crt_position,crt_time=queue.popleft()
        if crt_position==k:
            return crt_time
        next_p=[crt_position-1,crt_position+1,crt_position*2]
        for np in next_p:
            if 0<=np<=max and not visited[np]:
                visited[np]=True
                queue.append((np,crt_time+1))

n,k=map(int, input().split())
print(bfs(n,k))