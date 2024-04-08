def hanoi_tower(n, start, end, auxiliary):
    if n == 1:
        return 1, [(start, end)]  # 이동 횟수와 이동 과정 반환
    move_count1, moves1 = hanoi_tower(n-1, start, auxiliary, end)
    move_count2, moves2 = hanoi_tower(1, start, end, auxiliary)
    move_count3, moves3 = hanoi_tower(n-1, auxiliary, end, start)
    total_move_count = move_count1 + move_count2 + move_count3
    return total_move_count, moves1 + moves2 + moves3

# 입력 받기
N = int(input())

# 하노이 탑 알고리즘 실행
move_count, moves = hanoi_tower(N, 1, 3, 2)

# 이동 횟수 출력
print(move_count)

# 이동 과정 출력
for move in moves:
    print(move[0], move[1])
