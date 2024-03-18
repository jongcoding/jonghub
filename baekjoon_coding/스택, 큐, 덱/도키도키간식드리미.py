from collections import deque
def can_snack(num_list):
    stack=deque([])
    que=deque(num_list)
    for i in range(1, len(num_list)+1):
            if i in que:
                idx=que.index(i)
                for _ in range(idx):
                    stack.append(que.popleft())
                que.popleft()
            elif i in stack:
                if stack[-1]!=i:
                    return "Sad"
                else:
                    stack.pop()
    if not stack and not que:
        return "Nice"
n=int(input())
num_list=list(map(int, input().split()))
print(can_snack(num_list))
