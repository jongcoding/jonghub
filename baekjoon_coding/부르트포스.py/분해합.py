n=str(input())
a=list(n)
cha=[]
# 생성자 공식
# n1*100+n2*10+n3+n1+n2+n3
for i in range(1, len(a)*9+1):
    sum=0
    if int(n)>i:
        k=str(int(n)-i)
    else:
        break
    lk=list(k)
    for j in range(len(lk)):
        intk=int(lk[j])
        sum+=(10**(len(lk)-j-1))*intk+intk
    if sum==int(n):
        cha.append(int(k))
if cha==[]:
    print(0)
else:
    print(min(cha))
            

