import sys
N, X= map(int, sys.stdin.readline().split())
q=list(map(int, sys.stdin.readline().split()))
p=[]
for i in range(N):
    if q[i] < X:
        p.append(q[i])
sys.stdout.write(' '.join(map(str, p)))

# 최적화 코드
import sys

# 입력을 최적화합니다.
#N, X = map(int, sys.stdin.readline().split())
#q = list(map(int, sys.stdin.readline().split()))

# 필터링된 리스트를 생성합니다.
#p = [str(num) for num in q if num < X]

# 출력을 최적화합니다.
#sys.stdout.write(' '.join(p))