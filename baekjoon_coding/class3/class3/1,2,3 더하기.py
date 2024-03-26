t=int(input())
for _ in range(t):
    num=int(input())
    num_list=[1]*(num)
    count=1
    if num==1:
        print(1)
    elif num==2:
        print(2)
    elif num==3:
        print(4)
    else:
        dp=[0]*(num+1)
        dp[1]=1
        dp[2]=2
        dp[3]=4
        for i in range(4,num+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[num])
            
