from collections import deque

def bfs(l, current_p, move_p):
    visited = [[False] * l for _ in range(l)]
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    game = [[0] * l for _ in range(l)]
    start_y, start_x = current_p
    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = True
    
    while queue:
        y, x = queue.popleft()
        if (y, x) == (move_p[0], move_p[1]):
            return game[y][x]
        
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= nx < l and 0 <= ny < l and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
                game[ny][nx] = game[y][x] + 1
                
    return -1  

t = int(input())
for i in range(t):
    l = int(input())
    current_p = list(map(int, input().split()))
    move_p = list(map(int, input().split()))
    print(bfs(l, current_p, move_p))
