# math를 import 
import math 
a,b = map(int, input().split())
lcm=a*b//math.gcd(a,b)
print(lcm)

# 파이썬의 int는 파이썬의 기본 int 자료형은 매우 큰 정수를 처리할 수 있기 때문에 일반적인 상황에서는 이러한 제한이 없다.
