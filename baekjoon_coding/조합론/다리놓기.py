import math
n=int(input())

for _ in range(n):
    a,b=map(int, input().split())
    if a>b:
        print(math.factorial(a)//((math.factorial(a-b)*(math.factorial(b)))))
    else:
        print(math.factorial(b)//((math.factorial(b-a)*(math.factorial(a)))))
    