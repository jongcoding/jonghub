n=int(input())
a=input().split()
for i in range(1, 1000001):
    if n==1:
        print(int(a[0])**2)
        break
    else:
        j=0
        for num in a:
            if i%int(num)!=0: 
                j+=1
        if j==len(a) and i!=int(num):
            print(i)
            break