import sys
from bisect import bisect_left

# 입력 처리
input = sys.stdin.readline
N = int(input().strip())
A = list(map(int, input().strip().split()))

def longest_increasing_subsequence(A):
    dp = []  #
    parent = [-1] * N  
    lis_indices = []  

    for i in range(N):
        pos = bisect_left(dp, A[i])  
        if pos == len(dp):
            dp.append(A[i]) 
        else:
            dp[pos] = A[i]  
        
        # 인덱스 추적
        lis_indices.append(pos)
        if pos > 0:
            parent[i] = lis_indices[pos - 1]  

    lis_length = len(dp)


    lis = []
    index = lis_length - 1
    for i in range(N - 1, -1, -1):
        if lis_indices[i] == index:
            lis.append(A[i])
            index -= 1

    lis.reverse() 
    return lis_length, lis

length, sequence = longest_increasing_subsequence(A)

print(length)
print(' '.join(map(str, sequence)))
