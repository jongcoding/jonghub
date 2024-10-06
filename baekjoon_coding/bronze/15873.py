a=list(map(int, input()))
if len(a)==3:
    if a[0]==1 and a[1]==0:
        print(10+a[2])
    else:
        print(a[0]+10)    
elif len(a)==4:
    print(20)        
else:
    print(sum(a))
