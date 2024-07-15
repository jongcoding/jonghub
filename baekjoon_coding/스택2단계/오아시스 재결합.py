import sys
input = sys.stdin.readline

n = int(input().rstrip())
heights = [int(input().rstrip()) for _ in range(n)]

stack = []
count = 0

for h in heights:
    while stack and stack[-1][0]<h:
        
        count+=stack.pop()[1]

    if not stack:
        stack.append((h,1))

        continue

    if stack[-1][0]==h:
        same=stack.pop()[1]
        count+=same
        if stack:
            count+=1
        stack.append((h,same+1))
    else:
        stack.append((h,1))
        count+=1

print(count)
    
