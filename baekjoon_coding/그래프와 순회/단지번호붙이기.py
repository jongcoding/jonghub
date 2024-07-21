import sys
input = sys.stdin.readline

def dfs(x, y, map_grid, visited):
    stack = [(x, y)]
    count = 0
    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        count += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(map_grid) and 0 <= ny < len(map_grid) and not visited[nx][ny] and map_grid[nx][ny] == 1:
                stack.append((nx, ny))
    return count

n = int(input())
map_apart = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
num = 0
sizes = []

for i in range(n):
    for j in range(n):
        if map_apart[i][j] == 1 and not visited[i][j]:
            num += 1
            size = dfs(i, j, map_apart, visited)
            sizes.append(size)

sizes.sort()

print(num)
print('\n'.join(map(str, sizes)))
