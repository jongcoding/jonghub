import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
sequence_A = list(map(int, input().split())) ## queue == 0, stack == 1
sequence_B = list(map(int, input().split())) ## i번 자료구조에 들어있는 원소
M = int(input())                             ## 삽입할 수열의 길이
sequence_C = list(map(int, input().split())) ## 삽입할 수열

## 스택은 무시하고 큐만 deque에 추가하기
queue = deque([])
for i in range(N):
  if sequence_A[i] == 0:
    queue.appendleft(sequence_B[i])
else:
  if queue == []:
    print(*sequence_C)
    sys.exit()

## deque가 하나의 큐 처럼 작동
for i in range(M):
  queue.append(sequence_C[i])
  print(queue.popleft(), end = " ")