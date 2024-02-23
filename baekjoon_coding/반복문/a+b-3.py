T= int(input())
C= []

for i in range(T):
    A,B= map(int, input().split())
    C.append(A+B)
for i in range(T):
    print(C[i])

# 최적화 코드
#import sys

# 입력 최적화
#T = int(sys.stdin.readline())
#C = []

#for _ in range(T):
#   A, B = map(int, sys.stdin.readline().split())
#    C.append(A + B)

# 출력 최적화
#sys.stdout.write('\n'.join(map(str, C)))