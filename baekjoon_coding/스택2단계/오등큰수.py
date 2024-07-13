n = int(input())
a = list(map(int, input().split()))
num=[0]*(max(a)+1)
for i in a:
    num[i]+=1
result = [-1] * n 

stack = []  

for i in range(n):

    while stack and num[a[stack[-1]]]<num[a[i]]:
 
        result[stack.pop()] = a[i]

    stack.append(i)

print(" ".join(map(str, result)))