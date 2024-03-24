def fibonacci(n):
    fib =[[0,0]]*(n+2)
    fib[0]=[1,0] 
    fib[1]=[0,1]
    for i in range(2, n+1):
       fib[i]=[fib[i-1][0]+fib[i-2][0],fib[i-1][1]+fib[i-2][1]]
    return fib[n]

t= int(input())
for _ in range(t):
    n=int(input()) 
    a,b=fibonacci(n)
    print(a,b)
    