n=int(input())
people_time=list(map(int, input().split()))
people_time.sort()
sum_time=[0]*n
sum_time[0]=people_time[0]
for i in range(1,n):
    sum_time[i]=sum_time[i-1]+people_time[i]
print(sum(sum_time))