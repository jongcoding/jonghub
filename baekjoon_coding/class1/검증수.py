a,b,c,d,e=map(int,input().split())
print((a**2+b**2+c**2+d**2+e**2)%10)

# 최적화코드
numbers = list(map(int, input().split()))
result = sum(x**2 for x in numbers) % 10
print(result)
