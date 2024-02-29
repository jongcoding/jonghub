a=input()
b=a.upper()
c=list(set(b))
max=0
for i in range(len(c)):
    if b.count(c[i])>max:
        max=b.count(c[i])
        result=c[i]
    elif b.count(c[i])==max:
        result='?'
print(result)