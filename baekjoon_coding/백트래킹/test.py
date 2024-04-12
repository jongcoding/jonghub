import sys
def d_find(remain,start,total):
    global member_arr, N
    if remain == 0:
        if total > 0:
            total = -total
        global d_max
        if d_max < total:
            d_max = total
        return
    for i in range(start,N-remain):
        d_find(remain-1,i+1,total+member_arr[i])
input = sys.stdin.readline
N = int(input())
member_arr = list(map(int,input().split()))
member_arr[0] = sum(member_arr)
for i in range(1,N):
    line_arr = tuple(map(int,input().split()))
    for j in range(N):
        member_arr[j] = member_arr[j] + line_arr[j]
    member_arr[i] = member_arr[i] + sum(line_arr)
member_arr = tuple(sorted(member_arr,reverse = True))
total = -sum(member_arr)//2
d_max = total
d_find(N//2,0,total)
print(-d_max)