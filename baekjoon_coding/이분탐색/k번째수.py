n=int(input())
k=int(input())
a=[[x*y for x in range(1, n+1)] for y in range(1,n+1)]
start=0
end=k
result=0
while start<= end:
    mid=(start+end)//2
    temp=0
    for i in range(1, n+1):
        temp+=min(mid//i,n)
    if temp>=k:
        result=mid
        end=mid-1
    else:
        start=mid+1
print(result)