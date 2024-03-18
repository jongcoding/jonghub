import sys
while True:
    stack1=[]
    stack2=[]
    sentence=sys.stdin.readline()
    if sentence=='.':
        break
    list_sen=list(sentence)
    for word in list_sen:
        if word=='(':
            stack1.append(word)
        
        elif word=='[':
            stack2.append(word)

        elif word==']':
            if stack2:
                stack2.pop()
            else:
                sys.stdout.write("no")
        elif word==')':
            if stack1:
                stack1.pop()
            else:
                sys.stdout.write("no")
                break
        if len(stack1)<1 and len(stack2)<1:
            sys.stdout.write("yes")
            break
        else:
            sys.stdout.write("no")
            break



