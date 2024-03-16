import math

def count_open_windows(n):
    count_open = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # 약수의 개수가 홀수인 경우만 열려 있는 창문으로 간주합니다.
            if i != n // i:  # 제곱수인 경우를 제외합니다.
                count_open += 2
            else:
                count_open += 1
    return count_open

n = int(input())
print(count_open_windows(n))