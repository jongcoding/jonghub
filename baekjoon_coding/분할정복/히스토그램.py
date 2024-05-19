import sys
def largest_rectangle(n,h):
    stack=[]
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

input= sys.stdin.readline     
def main():
    n = int(input().rstrip())
    h = []
    for _ in range(n):
        h.append(int(input().strip()))
    print(largest_rectangle(n, h))

if __name__ == "__main__":
    main()