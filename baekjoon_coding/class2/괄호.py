#한 쌍의 괄호 기호가 된 ()문자열은 기본 VPS라고 함
# VPS 인지 아닌지 판단해야함
# 그럼 deque를 써서 첫번쨰로 나오는 '(', ')'를 제거해보는거임
# 만약 둘중에 하나가 남았다면 거짓임
def is_vps(sentense):
    stack=[]
    for word in sentense:
        if word =='(':
            stack.append(word)
        elif word==")":
            if not stack:
                return "NO"
            else:
                stack.pop()
    if stack:
        return "NO"
    else:
        return "YES"
t= int(input())
for _ in range(t):
    sentense=input()
    print(is_vps(sentense))
    
