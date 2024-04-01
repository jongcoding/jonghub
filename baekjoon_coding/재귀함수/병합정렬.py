count=0
def merge_sort(A, p, r, num_k):
    global count
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, num_k)
        merge_sort(A, q + 1, r, num_k)
        merge(A, p, q, r, num_k)
def merge(A,p, q, r, num_k):
    global count
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        count+=1
        if count==num_k:
            print(A[k])
            exit()

import sys
input=sys.stdin.readline
n, k = map(int, input().rstrip().split())
A=list(map(int, input().rstrip().split()))
merge_sort(A,0,len(A)-1, k)
if k>count:
    print(-1)

