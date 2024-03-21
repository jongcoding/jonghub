import sys
k,n=map(int, sys.stdin.readline().rstrip().split())
num_list=[]
for _ in range(k):
    num_list.append(int(sys.stdin.readline().rstrip()))
start, end=1, max(num_list)
result=0
while start<= end:
    mid =(start+end)//2
    count=0
    for cable in num_list:
        count+=cable//mid
    if count>=n:
        result=mid
        start=mid+1
    else:
        end= mid-1
print(result)