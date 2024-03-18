from collections import deque
n=int(input())
num_list=deque(list(map(int, input().split())))
que=deque(list(range(1,n+1)))
result=[]
for i in range(n):
    result.append(que.popleft())
    a=num_list.popleft()
    if a>0:
        num_list.rotate(-a+1)
        que.rotate(-a+1)
    else:
        num_list.rotate(-a)
        que.rotate(-a)
print(*result) 