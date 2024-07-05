def min_cost(M, memory, cost):
    MAX_COST=100*100+1
    dp=[0]*MAX_COST
    for i in range(n):
        mem=memory[i]
        c= cost[i]
        for j in range(MAX_COST-1,c-1,-1):
            dp[j]=max(dp[j], dp[j-c]+mem)
    for i in range(MAX_COST):
        if dp[i] >=M:
            return i


n, m = map(int, input().split())
app_memory = list(map(int, input().split()))
app_cost = list(map(int, input().split()))


print(min_cost(m, app_memory, app_cost))
