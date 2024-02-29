a=int(input())
b=int(input())
c=int(input())
e=list(str(a*b*c))
for i in range(10):
    print(e.count(str(i)))