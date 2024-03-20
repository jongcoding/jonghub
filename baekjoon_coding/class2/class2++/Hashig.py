r=31
m=1234567891
n=int(input())
array=list(input())
result=0
for i in range(n):
    ch=array[i]
    result+=(ord(ch)-96)*(r**i)
print(result%m)