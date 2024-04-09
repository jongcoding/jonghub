def backtracking(N, M, result, start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, N+1):
        result.append(i)
        backtracking(N, M, result, i + 1)
        result.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    result = []
    backtracking(N, M, result, 1)
