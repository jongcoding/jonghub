import heapq
import sys
input=sys.stdin.readline
def thief(jewels,bags,n):
    heap=[]
    total=0
    j=0
    for bag in bags:
        while j<n and jewels[j][0] <= bag:
            heapq.heappush(heap, -jewels[j][1])
            j+=1
        if heap:
            total-=heapq.heappop(heap)
    print(total)

n,k=map(int ,input().split())
jewels=[]
bags=[]
for _ in range(n):
    m,v=map(int, input().split())
    jewels.append([m,v])
for _ in range(k):
    bags.append(int(input()))
jewels.sort()
bags.sort()

thief(jewels,bags,n)