import sys
N,M = map(int, input().split())
backet=list(range(1, N+1))
for _ in range(M):
    i,j=map(int, sys.stdin.readline().split())
    q=backet[i-1:j]
    q.reverse()
    backet[i-1:j]=q
sys.stdout.write(' '.join(map(str, backet)))

# 최적화 코드
#import sys

# 입력 받기
#N, M = map(int, input().split())
#backet = list(range(1, N + 1))

# 연산 수행
#for _ in range(M):
#    i, j = map(int, sys.stdin.readline().split())
#    backet[i - 1:j] = reversed(backet[i - 1:j])

# 결과 출력
#sys.stdout.write(' '.join(map(str, backet)))