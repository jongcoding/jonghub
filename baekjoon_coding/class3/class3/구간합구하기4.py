import sys
input=sys.stdin.readline
n,m =map(int, input().rstrip().split())
num_list=list(map(int, input().split()))
cal_num=[0]*(n+1)
cal_num[1]=num_list[0]
for i in range(2, n+1):
    cal_num[i]=num_list[i-1]+cal_num[i-1]   
for _ in range(m):
    a,b=map(int,input().split())
    print(cal_num[b]-cal_num[a-1])