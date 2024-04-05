line = [['*']*3 for _ in range(3)]  # line 초기화

# 1,1 위치의 요소를 빈칸으로 만듦
start_x, end_x = 1, 1
start_y, end_y = 1, 1

for i in range(start_x, end_x + 1):
    for j in range(start_y, end_y + 1):
        line[i][j] = ' '

print(line)