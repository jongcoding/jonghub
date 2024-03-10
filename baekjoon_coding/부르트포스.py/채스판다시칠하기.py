n,m= map(int, input().split())
board=[input() for _ in range(n)]
counts=[]
# 체스판 찾기
for i in range(len(board)-7):
    for j in range(len(board[0])-7):
        count_b=0   # 맨왼쪽 위가 B인경우 카운트수
        count_w=0   # 맨왼쪽 위가 W인경우 카운트수
        # 체스판을 8*8로 잘라가며 검색
        for x in range(i, i+8):
            for y in range(j, j+8):
                # 맨 왼쪽 위가 'W'로 시작할 때의 칠하는 경우
                if (x + y - i - j) % 2 == 0:
                    if board[x][y] != 'W':
                        count_w += 1
                else:
                    if board[x][y] != 'B':
                        count_w += 1
                    
                if (x + y - i - j) % 2 == 0:
                    if board[x][y] != 'B':
                        count_b += 1
                else:
                    if board[x][y] != 'W':
                        count_b += 1
        counts.append(min(count_b,count_w))
print(min(counts))



                    
                