from collections import deque

def count_areas(normal, blindness):
    n = len(normal)
    normal_visited = [[False] * n for _ in range(n)]
    blindness_visited = [[False] * n for _ in range(n)]
    normal_areas = 0
    blindness_areas = 0
    
    # 방향 설정: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 구역을 탐색하는 함수
    def bfs(x, y, picture, visited):
        queue = deque([(x, y)])
        visited[x][y] = True
        color = picture[x][y]
        while queue:
            cx, cy = queue.popleft()            
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and picture[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    # 정상 시력인 경우와 적록색약인 경우 각각 구역 탐색
    for i in range(n):
        for j in range(n):
            if not normal_visited[i][j]:
                bfs(i, j, normal, normal_visited)
                normal_areas += 1
            if not blindness_visited[i][j]:
                bfs(i, j, blindness, blindness_visited)
                blindness_areas += 1
                
    return normal_areas, blindness_areas

# 입력 처리
n = int(input())
normal_picture = [list(input().rstrip()) for _ in range(n)]
blindness_picture = [[color if color != 'G' else 'R' for color in row] for row in normal_picture]

# 구역 수 계산
normal_areas, blindness_areas = count_areas(normal_picture, blindness_picture)

# 출력
print(normal_areas, blindness_areas)
