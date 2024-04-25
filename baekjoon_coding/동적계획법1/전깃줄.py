# 전기줄을 교차하지 않음
# 모든 전깃줄이 서로 교차하지않게 하기 위해 없애야 하는 젓깃줄 최소개수

def min_wire(n, electric_wire,wire):
    dp=[0 for _ in range(n)]
    dp[0]=wire[0]
    for start, end in wire:
        # 각자리에 전선의 갯수가 1보다 큰경우 
        if len(electric_wire[start])>1 or electric_wire[end]:
        # 전선이 교차하는 경우
        if:





n=int(input())

electric_wire=[[] for _ in range(501)]
wire=[]
for i in range(n):
    start, end=input().split()
    wire.append([start,end])
    electric_wire[int(start)]+=[int(end)]
print(electric_wire)
print(min_wire(n, electric_wire,wire))