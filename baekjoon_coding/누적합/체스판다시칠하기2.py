import sys
input = sys.stdin.read

# 입력 처리
data = input().split()
n, m, k = map(int, data[:3])
board = [data[i+3] for i in range(n)]

# 변경이 필요한 횟수를 계산하는 함수
def min_changes_to_chessboard():
    # 두 가지 색깔 패턴에 대한 변경 횟수를 저장할 배열 초기화
    changes_b = [[0] * (m + 1) for _ in range(n + 1)]
    changes_w = [[0] * (m + 1) for _ in range(n + 1)]

    # 누적합을 계산하며, 각 위치에서의 변경 횟수를 기록
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cell = board[i - 1][j - 1]
            # 홀수 위치와 짝수 위치가 서로 번갈아야 함
            expected_b = 'B' if (i + j) % 2 == 0 else 'W'
            expected_w = 'W' if (i + j) % 2 == 0 else 'B'
            changes_b[i][j] = changes_b[i - 1][j] + changes_b[i][j - 1] - changes_b[i - 1][j - 1] + (cell != expected_b)
            changes_w[i][j] = changes_w[i - 1][j] + changes_w[i][j - 1] - changes_w[i - 1][j - 1] + (cell != expected_w)

    # 최소 변경 횟수를 찾기
    min_changes = float('inf')
    for i in range(k, n + 1):
        for j in range(k, m + 1):
            repaint_b = changes_b[i][j] - changes_b[i - k][j] - changes_b[i][j - k] + changes_b[i - k][j - k]
            repaint_w = changes_w[i][j] - changes_w[i - k][j] - changes_w[i][j - k] + changes_w[i - k][j - k]
            min_changes = min(min_changes, repaint_b, repaint_w)

    return min_changes

# 결과 출력
print(min_changes_to_chessboard())
