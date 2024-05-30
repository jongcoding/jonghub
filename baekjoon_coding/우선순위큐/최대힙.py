import heapq
import sys
input =sys.stdin.readline

def max_heapq(n,cmd):
    result=[]
    max_heap=[]
    for i in range(n):
        if cmd[i]==0:
            if max_heap:
                result.append(-heapq.heappop(max_heap))
            else:
                result.append(0)
        else:
            heapq.heappush(max_heap, (cmd[i]) * -1)
    return result

if __name__=='__main__':
    n=int(input())
    cmd=[int(input()) for _ in range(n)]
    result=max_heapq(n,cmd)
    for num in result:
        print(num)