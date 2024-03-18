import sys
from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque([])

    def push_front(self, x):
        self.deque.appendleft(x)

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        if self.empty():
            return -1
        return self.deque.popleft()
    
    def pop_back(self):
        if self.empty():
            return -1
        return self.deque.pop()

    def size(self):
        return len(self.deque)
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.deque[0] 
    
    def back(self):
        if self.empty():
            return -1
        else:
            return self.deque[-1] 
    
    def empty(self):
        return 1 if not self.deque else 0


stack = Deque()

N = int(sys.stdin.readline())  # 주어지는 명령의 수
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == '1':
        stack.push_front(int(command[1]))

    elif command[0] == '2':
        stack.push_back(int(command[1]))
        
    elif command[0] == '3':
        sys.stdout.write(str(stack.pop_front()) + '\n')

    elif command[0] == '4':
        sys.stdout.write(str(stack.pop_back()) + '\n')

    elif command[0] == '5':
        sys.stdout.write(str(stack.size()) + '\n')

    elif command[0] == '6':
        sys.stdout.write(str(stack.empty()) + '\n')

    elif command[0] == '7':
        sys.stdout.write(str(stack.front()) + '\n')

    elif command[0] == '8':
        sys.stdout.write(str(stack.back()) + '\n')
        

# 출력 버퍼를 비워준다.
sys.stdout.flush()