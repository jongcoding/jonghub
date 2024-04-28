n,k =map(int, input().split())
num_list=list(map(int, input().split()))
current_sum=sum(num_list[:k])
max_sum=current_sum
for i in range(1,n-k+1):
    if k==1:
        print(max(num_list))
        exit()
    current_sum=current_sum-num_list[i-1]+num_list[i+k-1]
    max_sum=max(current_sum,max_sum)

print(max_sum)