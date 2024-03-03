n=int(input())
num_list=list(map(int, input().split()))
count=0
for num in num_list:
    ll=0
    for i in range(1,num//2+1):
        if num%i==0:
            ll+=1
    if ll==1:
        count+=1
print(count)




