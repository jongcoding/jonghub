from collections import deque
import sys
t=int(input())
for _ in range(t): 
    a=0
    p=list(sys.stdin.readline().rstrip())
    n=int(sys.stdin.readline().rstrip())
    num_array=deque(eval(sys.stdin.readline().rstrip()))
    reverse_count=0
    for let in p:
        if let=='R':
            reverse_count+=1
        elif let=='D':
            if num_array:
                if reverse_count%2==0:
                    num_array.popleft()
                else:
                    num_array.pop()
            else:
                a=1
                print("error")
                break
    if a==0: 
        if reverse_count%2==1:
            num_array.reverse()
        print('['+','.join(map(str, num_array))+']')