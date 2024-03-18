import sys
from collections import deque
k=int(sys.stdin.readline())
num_list=deque([])
for _ in range(k):
    num=int(sys.stdin.readline())
    if num==0:
        num_list.pop()
    else: 
        num_list.append(num)
print(sum(num_list))