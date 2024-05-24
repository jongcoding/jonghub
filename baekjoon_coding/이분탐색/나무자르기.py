import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
heights = list(map(int, input().split()))

start, end = 0, max(heights)
result = 0
h_count=Counter(heights)
while start <= end:
    mid = (start + end) // 2
    
    count = sum((height - mid)*count for height, count in h_count.items() if height > mid)  

    if count >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
