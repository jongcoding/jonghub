n = int(input())
a = list(map(int, input().split()))

result = [-1] * n  #  리스트를 -1로 초기화

stack = []  # 위치를 저장할 스택

for i in range(n):
    # 비어있지 않고 현재 원소가 스택의 최상단에 있는 원소보다 큰 경우
    while stack and a[stack[-1]] < a[i]:
        # 스택의 맨 위에 있는 원소가 현재 원소의 오큰수 
        result[stack.pop()] = a[i]
    
    # 현재 원소의 위치를 추가
    stack.append(i)

print(" ".join(map(str, result)))
