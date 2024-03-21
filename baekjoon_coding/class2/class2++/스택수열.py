import sys
n=int(sys.stdin.readline().rstrip())
num_list=[]
stack=[]
result=[]
for _ in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))
i=1
for num in num_list:
    while True:
        if num>=i:
            stack.append(i)
            result.append("+")
            i+=1
        elif num==stack[-1]:
            stack.pop()
            result.append("-")
            break
        else:
            print("NO")
            sys.exit()
print("\n".join(map(str, result)))