import sys

# 입력 받기
N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

# 중앙값 찾기
median = sorted(numbers)[N // 2]

# 최빈값 찾기
count = [0] * 8001  # -4000부터 4000까지의 숫자를 담을 수 있는 배열 생성
for num in numbers:
    count[num + 4000] += 1
max_count = max(count)
mode_candidates = [idx - 4000 for idx, c in enumerate(count) if c == max_count]
mode = min(mode_candidates) if len(mode_candidates) == 1 else sorted(mode_candidates)[1]

# 산술평균 구하기
mean = sum(numbers) / N

# 범위 구하기
range_ = max(numbers) - min(numbers)

# 결과 출력
print(round(mean))  # 산술평균
print(median)       # 중앙값
print(mode)         # 최빈값
print(range_)       # 범위