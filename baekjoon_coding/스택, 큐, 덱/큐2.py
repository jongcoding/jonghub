# sys.stdin.readline()
# sys.stdout.write() 를 쓰는게 더빠르다
import sys
from collections import deque

class Que:
    def __init__(self):
        self.que = deque([])

    def push(self, x):
        self.que.append(x)

    def pop(self):
        if self.empty():
            return -1
        return self.que.popleft()

    def size(self):
        return len(self.que)
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.que[0] 
    
    def back(self):
        if self.empty():
            return -1
        else:
            return self.que[-1] 
    
    def empty(self):
        return 1 if not self.que else 0


stack = Que()

N = int(sys.stdin.readline())  # 주어지는 명령의 수
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        sys.stdout.write(str(stack.pop()) + '\n')
    elif command[0] == 'size':
        sys.stdout.write(str(stack.size()) + '\n')
    elif command[0] == 'empty':
        sys.stdout.write(str(stack.empty()) + '\n')
    elif command[0] == 'front':
        sys.stdout.write(str(stack.front()) + '\n')
    elif command[0] == 'back':
        sys.stdout.write(str(stack.back()) + '\n')

# 출력 버퍼를 비워준다.
sys.stdout.flush()