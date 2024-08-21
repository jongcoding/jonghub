from collections import deque
n,m,h=map(int, input().split())
tomato=[[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]

def bfs(tomato):
    count=0
    stack=deque([])
    visited=[[[False]*n for _ in range(m)] for _ in range(h)]
    for z in range(h):
        for y in range(m):
            for x in range(n):
                if tomato[z][y][x]==1:
                    stack.append((z,y,x))
                    visited[z][y][x]=True
    
    dir=[(0,-1,0),(0,1,0),(0,0,1),(0,0,-1),(1,0,0),(-1,0,0)]
    
    while stack:
        for _ in range(len(stack)):
            z,y,x=stack.popleft()
            for dz,dy,dx in dir:
                nz, ny, nx = z + dz, y + dy, x + dx
                if 0 <= nz < h and 0 <= ny < m and 0 <= nx < n:
                    if tomato[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                        tomato[nz][ny][nx] = 1
                        visited[nz][ny][nx] = True
                        stack.append((nz, ny, nx))
        if stack:
            count+=1

    for z in range(h):
        for y in range(m):
            for x in range(n):
                if tomato[z][y][x]==0:
                    return -1
    return count

print(bfs(tomato))