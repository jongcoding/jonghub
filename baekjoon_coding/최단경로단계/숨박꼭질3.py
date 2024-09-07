import sys
input=sys.stdin.readline
def find(n,k):
    if k<=n:
        return n-k
    elif n==0:
        return 1+find(n+1,k)
    elif k%2==0:
        return min(k-n, find(n,k//2))
    else:
        return 1+min(find(n,k-1),find(n,k+1))
n,k=map(int, input().rstrip().split())
print(find(n,k))