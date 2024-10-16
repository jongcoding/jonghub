n=int(input())

for i in range(1,n):
    print(" "*abs(n-i)+"*"*i)
for j in range(n,0,-1):
    print(" "*abs(n-j)+"*"*j)