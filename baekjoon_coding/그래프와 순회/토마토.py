from collections import deque
n,m=map(int, input().split())
tomato=[list(map(int, input().split())) for _ in range(m)]
def bfs(tomato):
    count=0
    stack=deque([])
    visited=[[False]*n for _ in range(m)]
    for y in range(m):
        for x in range(n):
            if tomato[y][x]==1:
                stack.append((y,x))
                visited[y][x]=True
    
    dir=[(-1,0),(1,0),(0,1),(0,-1)]
    
    new_stack=[]
    while stack:
        y,x=stack.popleft()
        for dy,dx in dir:
            if 0<=(y+dy)<m and 0<=(x+dx)<n:
                if tomato[y+dy][x+dx]==0 and visited[y+dy][x+dx]==False:
                    tomato[y+dy][x+dx]=1
                    visited[y+dy][x+dx]=True
                    new_stack.append((y+dy,x+dx))
        if not stack:
            if new_stack:
                stack=deque(new_stack)
                new_stack=[]
                count+=1
            else:
                for y in range(m):
                    for x in range(n):
                        if tomato[y][x]==0:
                            return -1
                return count 
    for y in range(m):
        for x in range(n):
            if tomato[y][x]==0:
                return -1
    return count

print(bfs(tomato))

