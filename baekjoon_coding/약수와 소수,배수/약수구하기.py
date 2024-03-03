n,k=map(int,input().split())
# n의 약수중 k번째로 작은 수 출력
num=0

for i in range(1,n+1):
    if n%i==0:
        num+=1
    if num==k:
        print(i)
        break
if num<k:
    print(0)
