import sys
N, M= map(int, sys.stdin.readline().split())
Backet=[0]*N
for number in range(N):
    Backet[number]=number+1

for _ in range(M):
    i,j = map (int, sys.stdin.readline().split())
    Backet[i-1] , Backet[j-1]= Backet[j-1], Backet[i-1]
sys.stdout.write(' '.join(map(str, Backet)))

# 최적화 코드
#import sys

# 입력 받기
#input_line = sys.stdin.readline().split()
#N, M = map(int, input_line)

# 초기화
#Bucket = list(range(1, N + 1))

# 교환 수행
#for _ in range(M):
#    input_line = sys.stdin.readline().split()
#    i, j = map(int, input_line)
#    Bucket[i - 1], Bucket[j - 1] = Bucket[j - 1], Bucket[i - 1]

# 결과 출력
#print(*Bucket)