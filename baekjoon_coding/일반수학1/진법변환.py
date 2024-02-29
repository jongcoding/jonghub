N,B=input().split()
q=list(N)
result=0
for i in range(len(N)):
    if q[i].isdigit():
        result+=int(q[i])*((int(B)**(len(N)-i-1)))
    else:
        result+=(ord(q[i])-55)*(int(B)**(len(N)-i-1))
print(result)

# 최적화 코드
N, B = input().split()
result = 0

for digit in N:
    if digit.isdigit():
        result = result * int(B) + int(digit)
    else:
        result = result * int(B) + ord(digit) - 55

print(result)
