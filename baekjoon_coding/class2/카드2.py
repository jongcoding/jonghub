#n장의 카드
# 제일 위에 있는 카드 버리고 제일 위에 있는 카드를 맨 밑에 둔다.
# deque를 사용해보자 list보다 빠르다

from collections import deque
n=int(input())
num_list=deque(range(1, n+1))
while len(num_list)>1:
    num_list.popleft()
    num_list.append(num_list.popleft())
print(num_list[0])