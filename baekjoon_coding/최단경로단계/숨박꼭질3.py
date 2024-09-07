import sys
input =sys.stdin.readline
def bfs(n,k):
    if k<=n:
        return n-k
    elif n==0:
        return 1+bfs(n+1,k)
    elif k%2==0:
        return min(k-n, bfs(n,k//2))
    else:
        return 1+min(bfs(n,k-1), bfs(n+1,k+1))
def main():
    n,k=map(int, input().split())
    print(bfs(n,k))
if __name__=="__main__":
    main()