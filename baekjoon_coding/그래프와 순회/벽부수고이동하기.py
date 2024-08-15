from collections import deque

def bfs(n, m, grid):
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    
    while queue:
        x, y, wall_broken = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall_broken]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and visited[nx][ny][wall_broken] == 0:
                    visited[nx][ny][wall_broken] = visited[x][y][wall_broken] + 1
                    queue.append((nx, ny, wall_broken))
                if grid[nx][ny] == 1 and wall_broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][wall_broken] + 1
                    queue.append((nx, ny, 1))
    
    return -1

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
print(bfs(n, m, grid))
