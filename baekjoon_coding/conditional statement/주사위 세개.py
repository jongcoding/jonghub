a,b,c=map(int,input().split())
d=sorted([a,b,c], reverse=True)
if a==b==c:
    print(a*1000+10000)
elif a==b or b==c or c==a:
    print(1000+d[1]*100)
else:
    print(d[0]*100)


    