T= int(input())
C= []

for i in range(T):
    A,B= map(int, input().split())
    C.append(A+B)
for i in range(T):
    print(C[i])

# 최적화 코드
# for _ in range(int(input())):
#    print(sum(map(int, input().split())))