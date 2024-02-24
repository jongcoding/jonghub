import sys
N,M=map(int, sys.stdin.readline().split())
b=[0]*N # 배열 초기화
for _ in range(M):
    i,j,k=map(int, sys.stdin.readline().split())
    for num in range(i, j+1):
        b[num-1]=k
sys.stdout.write(' '.join(map(str, b)))