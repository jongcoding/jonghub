import math
n=int(input())
a=input().split()
b=list(int(x) for x in a)
what_lcm=b[0]
if len(a)==1:
    print(b[0]**2)
    exit()
for i in range(len(b)-1):
    what_lcm=math.lcm(what_lcm,b[i+1])
if what_lcm in b:
    what_lcm=what_lcm*min(b)
print(what_lcm)
    