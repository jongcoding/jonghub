def count_worms(m, n, k, cabbage_positions):
    from collections import deque


    farm = [[0]*m for _ in range(n)]
    

    for x, y in cabbage_positions:
        farm[y][x] = 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y)])
        farm[start_y][start_x] = 0  
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and farm[ny][nx] == 1:
                    farm[ny][nx] = 0  
                    queue.append((nx, ny))
    
    worm_count = 0
    for y in range(n):
        for x in range(m):
            if farm[y][x] == 1:  
                bfs(x, y)
                worm_count += 1

    return worm_count


t = int(input())
results = []
for _ in range(t):
    m, n, k = map(int, input().split())
    cabbage_positions = [tuple(map(int, input().split())) for _ in range(k)]
    result = count_worms(m, n, k, cabbage_positions)
    results.append(result)


for result in results:
    print(result)
