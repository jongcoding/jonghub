x=int(input())
n=1
while True:
    q=int((n+1)*(n)/2)
    if q>=x:
        if (n-1)%2!=0:
            result=str(n-q+x)+"/"+str(1+(q-x))
        else:
            result=str(1+(q-x))+"/"+str(n-(q-x))
        break
    elif x==1:
        result="1/1"
        break
    else:
        n+=1
print(result)
# 최적화 코드
import math

x = int(input())

if x == 1:
    result = "1/1"
else:
    n = math.ceil((-1 + math.sqrt(1 + 8 * x)) / 2)
    q = n * (n + 1) // 2
    if (n - 1) % 2 != 0:
        result = f"{n - (x - q)}/{1 + (x - q)}"
    else:
        result = f"{1 + (x - q)}/{n - (x - q)}"

print(result)
