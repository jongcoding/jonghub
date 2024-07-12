string=input()
frula=input()
frula_len=len(frula)
stack=[]
for char in string:
    stack.append(char)
    if len(stack)>=frula_len and ''.join(stack[-frula_len:])==frula:
        for _ in range(frula_len):
            stack.pop()
result=''.join(stack)
if not result:
    print("FRULA")    
else:
    print(result)