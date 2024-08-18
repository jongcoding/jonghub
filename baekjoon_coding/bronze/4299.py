def find_scores(S, D):
    if (S + D) % 2 != 0 or (S - D) % 2 != 0:
        return -1
    
    x = (S + D) // 2
    y = (S - D) // 2
    
    if x < 0 or y < 0:
        return -1
    
    if x >= y:
        return (x, y)
    else:
        return (y, x)

S, D = map(int, input().strip().split())

result = find_scores(S, D)
if result == -1:
    print(-1)
else:
    print(result[0], result[1])