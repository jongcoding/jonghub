from collections import deque
def count_computer(computer_list, computer_num):
    visited=[False]*(computer_num+1)
    queue=deque([1])
    visited[1]=visited
    count=0 
    while queue:
        start= queue.popleft()
        for i in range(computer_num+1):
            if not visited[i] and (start, i) in computer_list:
                visited[i]=True
                count+=1
                queue.append(i)
    return count

computer_num=int(input())
computer_pairs=int(input())
computer_list=[]
for _ in range(computer_pairs):
    a,b=map(int, input().split())
    computer_list.append((a,b))
    computer_list.append((b,a))
print(count_computer(computer_list, computer_num))

