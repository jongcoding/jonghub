def mul(i, end):
    return end >= i * 2

def sq(end, new_num):
    return end >= new_num

start, end = map(int, input().split())
dp = {}
dp[start] = 1

queue = [start]  

while queue:
    i = queue.pop(0)
    new_num = i * 10 + 1 
    if mul(i, end):
        if i * 2 not in dp:
            dp[i * 2] = dp[i] + 1
            queue.append(i * 2)
        else:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    if sq(end, new_num):
        if new_num not in dp:
            dp[new_num] = dp[i] + 1
            queue.append(new_num)
        else:
            dp[new_num] = min(dp[new_num], dp[i] + 1)

if end in dp:
    print(dp[end])
else:
    print(-1)
