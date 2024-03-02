n=int(input())
square=4
result=2
for i in range(n):
    result=result+2**i
print(result*result)

# 최적화 코드
n = int(input())
result = 2 ** (n + 1) - 1
print(result * result)
