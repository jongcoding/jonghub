import heapq
import sys
input=sys.stdin.readline
def min_heapq(n, cmd):
    result=[]
    min_heap=[]

    for i in range(n):
        if cmd[i]==0:
            if min_heap:
                result.append(heapq.heappop(min_heap))
            else:
                result.append(0)
        else:
            heapq.heappush(min_heap,cmd[i])
    return result

def main():
    n= int(input())
    cmd=[int(input()) for _ in range(n)]
    results=min_heapq(n,cmd)
    for result in results:
        print(result)
if __name__=='__main__':
    main()