# 1. 좌표(i,j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.(2초)
# 2. 인벤토리에서 블록 하나를 꺼내어 좌표(i,j)의 가장 위에 있는 블록위에 놓는다.(1초)

# 땅의 높이는 256보다 작아야한다.
import sys
from collections import Counter
N,M,B=map(int, sys.stdin.readline().split())
land=[]
for _ in range(N):
    land.extend(list(map(int, sys.stdin.readline().split())))
blocks=Counter(land)
ret=[]
for target in range(max(blocks.keys()),-1,-1):
    time=0
    inventory=B
    need=0
    for gh, gc in blocks.items():
        if target <gh:
            inventory+=(gh-target)*gc
            time+=2*(gh-target)*gc
        elif target> gh:
            need+=(target-gh)*gc
            time+= (target-gh)*gc
    if inventory>=need:
        ret.append([time,target])
ret.sort(key=lambda x: (x[0], -x[1])) 
print(ret[0][0],ret[0][1])