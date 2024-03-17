# 이항계수는 nCk로 표현가능(조합)
# n!/k!(n-k)! 공식이다.
# math 라이브러리 factorial을 사용해보자
import math

def combination(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

n, k = map(int, input().split())
print(combination(n, k))
