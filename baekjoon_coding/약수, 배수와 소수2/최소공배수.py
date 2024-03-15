# math를 import 
import math 
t= int(input())
for _ in range(t):
    a,b = map(int, input().split())
    lcm=a*b//math.gcd(a,b)
    print(lcm)

# gcd(a,b): # 최대 공약수
#       while b:
#           a,b=b,a%b
#       return a