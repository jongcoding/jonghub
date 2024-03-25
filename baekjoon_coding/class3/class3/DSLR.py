from collections import deque
def command(start,command):
    if command=="D":
        return (start*2)%10000
    elif command=="S":
        if start == 0: return 9999
        return start - 1
    elif command=="L":
        return (start % 1000) * 10 + start // 1000
    elif command=="R":
        return (start % 10) * 1000 + start // 10   
    
def find_shortest_path(start, end):
    queue = deque([(start, "")])
    visited = set([start])

    while queue:
        num, path = queue.popleft()

        for com in ["D", "S", "L", "R"]:
            next_num = command(num, com)
            if next_num not in visited:
                visited.add(next_num)
                new_path = path + com
                queue.append((next_num, new_path))

                if next_num == end:
                    return new_path

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(find_shortest_path(A, B))