import sys
def input(): return sys.stdin.readline().rstrip()

def dfs(idx):
    if idx >= len(empty_cells):
        return True   
    i,j = empty_cells[idx]
    r,c = (i //3) * 3, (j //3) * 3
    nums1 = set([1,2,3,4,5,6,7,8,9])
    nums2 = set(board[i] + [board[k][j] for k in range(9)] + board[r][c:c+3] + board[r+1][c:c+3] + board[r+2][c:c+3])
    for num in nums1 - nums2:
        board[i][j] = num
        if dfs(idx+1): return True
        board[i][j] = 0
    return False
board = []
empty_cells = []    
for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(9):
        if row[j] == 0:
            empty_cells.append((i, j))

dfs(0)

for i in range(9):
    print(*board[i])
