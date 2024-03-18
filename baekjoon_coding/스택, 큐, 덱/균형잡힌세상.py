def is_vps(sentense):
    stack=[]
    for word in sentense:
        if word =='(':
            stack.append(word)
        elif word==")":
            if not stack:
                return "no"
            elif stack[-1]!='(':
                return "no"
            else:
                stack.pop()
        elif word=='[':
            stack.append(word)
        elif word==']':
            if not stack:
                return "no"
            elif stack[-1]!='[':
                return "no"
            else:
                stack.pop()
    if stack:
        return "no"
    else:
        return "yes"
import sys
while True:
    sentence=sys.stdin.readline().rstrip()
    if sentence==".":
        break
    sys.stdout.write(is_vps(sentence)+'\n')
    



