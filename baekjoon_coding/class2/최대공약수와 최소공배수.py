# 두 개의 자연수를 입력
# 최대 공약수와 최소 공배수 출력
# math 라이브러리 사용해보기
import math
a,b= map(int,input().split())
print(math.gcd(a,b))    # 최대 공약수
print(math.lcm(a,b))    # 최소 공배수
