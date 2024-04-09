def solve_n_queen(board, row, N, count, col_safe, diag1_safe, diag2_safe):
    if row == N:
        return count + 1
    
    for col in range(N):
        if col_safe[col] and diag1_safe[row + col] and diag2_safe[row - col + N - 1]:
            board[row][col] = 1
            col_safe[col] = diag1_safe[row + col] = diag2_safe[row - col + N - 1] = False
            count = solve_n_queen(board, row + 1, N, count, col_safe, diag1_safe, diag2_safe)
            board[row][col] = 0
            col_safe[col] = diag1_safe[row + col] = diag2_safe[row - col + N - 1] = True
    
    return count

if __name__ == "__main__":
    N = int(input())
    board = [[0] * N for _ in range(N)]
    col_safe = [True] * N
    diag1_safe = [True] * (2 * N - 1)
    diag2_safe = [True] * (2 * N - 1)
    count = 0
    count = solve_n_queen(board, 0, N, count, col_safe, diag1_safe, diag2_safe)
    print(count)