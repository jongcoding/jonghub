from collections import deque

def bfs(mirro,n,m):
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    visited=[[False]*m for _ in range(n)]
    queue = deque([(0,0)])
    visited[0][0] = True
    while queue:
        x,y = queue.popleft()
        if x==n-1 and y==m-1:
            return mirro[x][y]
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx <n and 0 <=ny<m and mirro[nx][ny]==1 and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                mirro[nx][ny]=mirro[x][y]+1
    return -1

n,m=map(int, input().split())
mirro=[list(map(int,str(input()))) for _ in range(n)]
print(bfs(mirro,n,m))