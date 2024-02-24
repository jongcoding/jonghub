N=int(input())
q=str(input())
sum=0
for i in range(N):
    sum=sum+int(q[i])
print(sum)

#최적화 코드
# input()
# print(sum(map(int, input())))