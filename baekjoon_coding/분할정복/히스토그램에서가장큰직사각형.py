# 내가 생각한 알고리즘 처음 높이측정
# 그리고 그다음 히스토그램 높이 측정, 그리고 전 히스토그램이랑 높이 파악 
# 만약 전보다 크다면 전 높이로 가로길이 곱한 값을 직사각형에 넣어버림
# 만약 전보다 작다면 현 높이로 가로길이 곱한 값을 직사각형에 넣어버림
# 만약 전이랑 같아면 해당 높이로 가로길이 곱한 값을 직사가형에 넣음

import sys

def longest_rect(n,h):

    stack=[]
    max_rect=0
    index=0
    while index<n:
        if not stack or h[stack[-1]]<=h[index]:
            stack.append(index) 
            index+=1
        else:
            top=stack.pop()
            if not stack:
                x=index
            else:
                x=index-stack[-1]-1
            y=h[top]
            area=x*y
            max_rect=max(area,max_rect)
    while stack:
        top=stack.pop()
        if not stack:
            x=index
        else:
            x=index-stack[-1]-1
        y=h[top]
        area=x*y
        max_rect=max(area,max_rect)       
    return max_rect
def main():
    input =sys.stdin.readline
    while True:
        test=list(map(int, input().rstrip().split()))
        if test==[0]:
            break
        n=test[0]
        h=test[1:]
        print(longest_rect(n,h))
    

if __name__=='__main__':
    main()