#입력 계수가 낮고 메모리가 한정적일떄 효율적인 계수정렬

import sys

# 입력 받기
N = int(input())  # 수의 개수 N 입력 받기

# 카운트 배열 초기화
count = [0] * 10001  # 수의 범위가 1부터 10,000까지이므로

# 각 수의 등장 횟수를 카운트 배열에 저장
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    count[num] += 1

# 정렬된 결과 출력
for i in range(1, 10001):  # 수의 범위가 1부터 10,000까지이므로
    for _ in range(count[i]):
        print(i)