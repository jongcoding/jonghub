import sys
input= sys.stdin.readline


def star(n, star_board):
    interval=n//3
    start_x,start_y=n//3, n//3
    end_x,end_y=start_x+interval,start_y+interval
    blank(interval, start_x, end_x, start_y, end_y, star_board)
    return star_board
def blank(interval, start_x, end_x, start_y, end_y, star_board):
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            star_board[i][j]==' '
    if interval==1:
        return star_board
    interval=interval//3
    for i in range(3):
        for j in range(3):
            blank(interval, start_x-interval//3*2+j*interval,start_x-interval//3+j*interval,start_y-interval//3*2+i*interval, start_y-interval//3+i*interval, star_board)
            #blank(interval, end_x+interval//3+, end_x+interval//3*2, end_y+interval//3, end_y+interval//3*2, star_board)
# n은 3의 거듭 제곱 1~7 
n=int(input().rstrip())
star_board=[['*']*n for _ in range(n)]
for i in range(n):
    print(''.join(map(str, star_board[i])))
star(n, star_board)
for i in range(n):
    print(''.join(map(str, star_board[i])))