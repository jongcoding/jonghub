n, m = map(int, input().split())
card_list=list(map(int, input().split()))
card_list.sort()
sum_list=[]
for i in range(n): 
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum=card_list[i]+card_list[j]+card_list[k]
            if m>=sum:
                sum_list.append(sum)
print(max(sum_list))