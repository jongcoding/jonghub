n=int(input())
q=0
result=1
while True:
    result=3*q*(q-1)+1
    if n-result>0:
        q+=1
    elif n==1:
        q=1
        break
    else:
        break
print(q)

# 최적화 코드
import math

n = int(input())
if n == 1:
    q = 1
else:
    q = math.ceil((3 + math.sqrt(5)) / 3)
print(q)
