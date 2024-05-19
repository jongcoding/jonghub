# 내가 생각한 알고리즘 처음 높이측정
# 그리고 그다음 히스토그램 높이 측정, 그리고 전 히스토그램이랑 높이 파악 
# 만약 전보다 크다면 전 높이로 가로길이 곱한 값을 직사각형에 넣어버림
# 만약 전보다 작다면 현 높이로 가로길이 곱한 값을 직사각형에 넣어버림
# 만약 전이랑 같아면 해당 높이로 가로길이 곱한 값을 직사가형에 넣음

from collections import deque
def largest_rectangle(n,h):
    stack=deque([])
    max_area=0
    index=0
    while index <n:
        # 전에 깔려 있던 것보다 크거나 같을때
        if not stack or h[stack[-1]]<=h[index]:
            stack.append(index)
            index+=1

        # 전보다 작을 때
        else:
            top =stack.pop()
            area=(h[top]*((index-stack[-1]-1) if stack else index))
            max_area=max(max_area,area)

    while stack:
        top=stack.pop()
        area=(h[top]*((index-stack[-1]-1) if stack else index))
        max_area=max(max_area,area)

    return max_area
            
while True: 

    input_number= list(map(int, input().split()))
    if input_number==[0]:
        exit()    
    h=deque(input_number)
    n=h.popleft()
    print(largest_rectangle(n,h))
   