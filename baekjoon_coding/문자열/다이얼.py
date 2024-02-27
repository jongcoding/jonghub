a=input()
num=0
for i in range(len(a)):
    if a[i]=='A'or a[i]=='B' or a[i]=='C':
        num+=3
    elif a[i]=='D'or a[i]=='E' or a[i]=='F':
        num+=4
    elif a[i]=='G'or a[i]=='H' or a[i]=='I':
        num+=5
    elif a[i]=='J'or a[i]=='K' or a[i]=='L':
        num+=6
    elif a[i]=='M'or a[i]=='N' or a[i]=='O':
        num+=7
    elif a[i]=='P'or a[i]=='Q' or a[i]=='R' or a[i]=='S':
        num+=8
    elif a[i]=='T'or a[i]=='U' or a[i]=='V':
        num+=9
    elif a[i]=='W'or a[i]=='X' or a[i]=='Y'or a[i]=='Z' :
        num+=10
print(num)

# 최적화 코드
#num = sum(3 + (ord(char) - ord('A')) // 3 for char in input().upper() if 'A' <= char <= 'Z')
#print(num)