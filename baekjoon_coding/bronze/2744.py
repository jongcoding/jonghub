# 주어진 문자열
s=input()
b=[]
# 문자열의 각 문자를 확인
for char in s:
    if char.isupper():
        b.append(char.lower())
    elif char.islower():
        b.append(char.upper())
    else:
        b.append(char)

print(''.join(map(str, b)))
