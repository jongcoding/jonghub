from collections import deque

def build_board(ladders, snakes):
    board = [0] * 101
    for start, end in ladders:
        board[start] = end
    for start, end in snakes:
        board[start] = end
    return board

def min_dice_rolls(ladders, snakes):
    board = build_board(ladders, snakes)
    visited = [False] * 101
    queue = deque([(1, 0)])  # (position, rolls)
    visited[1] = True

    while queue:
        position, rolls = queue.popleft()
        if position == 100:
            return rolls
        for i in range(1, 7):
            next_position = position + i
            if next_position <= 100 and not visited[next_position]:
                visited[next_position] = True
                if board[next_position]:
                    next_position = board[next_position]
                queue.append((next_position, rolls + 1))

    return -1

def main():
    N, M = map(int, input().split())
    ladders = [tuple(map(int, input().split())) for _ in range(N)]
    snakes = [tuple(map(int, input().split())) for _ in range(M)]

    min_rolls = min_dice_rolls(ladders, snakes)
    print(min_rolls)

if __name__ == "__main__":
    main()
