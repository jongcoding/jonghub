n=int(input())
square=[]
num=0
for _ in range(n):
    x,y = map(int, input().split())
    for dot_x in range(10):
        for dot_y in range(10):
            if [dot_x+x,dot_y+y] in square:
                pass
            else:
                square.append([dot_x+x,dot_y+y])
                num+=1
print(num)

# 최적화 코드
n = int(input())
coordinates = set()
num = 0

for _ in range(n):
    x, y = map(int, input().split())
    for dot_x in range(x, x + 10):
        for dot_y in range(y, y + 10):
            if (dot_x, dot_y) not in coordinates:
                coordinates.add((dot_x, dot_y))
                num += 1

print(num)