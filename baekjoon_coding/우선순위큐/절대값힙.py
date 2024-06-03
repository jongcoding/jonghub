import heapq
import sys
input=sys.stdin.readline

def absolute_value_hip(n,cmd):
    result=[]
    minus=[]
    plus=[]
    for i in cmd:
        if i==0:
            if minus and (not plus):
                result.append(-heapq.heappop(minus))

            elif plus and (not minus):
                result.append(heapq.heappop(plus))

            elif minus and plus:

                if plus[0]>= minus[0]: 
                    result.append(-heapq.heappop(minus))
                    
                else:
                    result.append(heapq.heappop(plus))

            else:
                result.append(0)
            
        else:
            if i>0:
                heapq.heappush(plus, i)
            else:
                heapq.heappush(minus, -i)
    
    return result

def main():
    n=int(input())
    cmd=[int(input()) for _ in range(n)]
    results=absolute_value_hip(n,cmd)
    for result in results:
        print(result)

if __name__ =='__main__':
    main()