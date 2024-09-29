def count_sticks(X):
    count = 0
    while X > 0:
        if X & 1:
            count += 1
        X >>= 1
    return count

X = int(input())
print(count_sticks(X))
