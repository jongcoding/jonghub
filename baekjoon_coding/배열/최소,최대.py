import sys
N=int(sys.stdin.readline())
q=list(map(int, sys.stdin.readline().split()))
print(min(q),max(q))

# 최적화 코드
#import sys

# 입력을 최적화합니다.
#N = int(sys.stdin.readline())
#q = list(map(int, sys.stdin.readline().split()))

# 최솟값과 최댓값을 계산합니다.
#min_value = min(q)
#max_value = max(q)

# 출력을 최적화합니다.
#sys.stdout.write("%d %d\n" % (min_value, max_value))