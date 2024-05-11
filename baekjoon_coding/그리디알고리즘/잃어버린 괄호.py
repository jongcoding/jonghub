#괄호를 적절히 쳐서 식을 최소값을 만드는 것
a=input().split("-")
for i in range(len(a)):
    a[i]=sum(list(map(int,a[i].split("+"))))
start=a[0]
for i in range(1,len(a)):
    start-=a[i]
print(start)