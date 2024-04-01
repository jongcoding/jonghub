def fibonachi(n):
    
    if n==0:
        return 0
    
    elif n==1:
        return 1
    
    elif n>=2:
        num_list=[0]*(n+1)
        num_list[1]=1 
        for i in range(2,n+1):
            num_list[i]=num_list[i-1]+num_list[i-2]
        return num_list[n]
n=int(input())
print(fibonachi(n))


