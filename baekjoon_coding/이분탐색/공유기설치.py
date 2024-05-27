import sys
def passible(x, mid, c, n):
    count = 1
    last = x[0]

    for i in range(1, n):
        if x[i] - last >= mid:
            count += 1
            last = x[i]
            if count >= c:
                return True
    return False

def find_min(n, c, x):
    x.sort()
    start = 1
    end = x[-1] - x[0]
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if passible(x, mid, c, n):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

# 입력 처리
input=sys.stdin.readline
n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]

# 결과 출력
print(find_min(n, c, x))
