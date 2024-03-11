# 입력 받기
N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# 점을 정렬하기
def custom_sort(point):
    return (point[1], point[0])

sorted_points = sorted(points, key=custom_sort)
#sorted_points = sorted(points, key=lambda point: (point[1], point[0]))
# 정렬된 점 출력하기
for point in sorted_points:
    print(point[0], point[1])
