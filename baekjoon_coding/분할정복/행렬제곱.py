p = 1000

def matrix_multiply(A, B, n):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= p
    return result

def matrix_power(matrix, n, b):
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = matrix.copy()

    while b > 0:
        if b % 2 == 1:
            result = matrix_multiply(result, base, n)
        base = matrix_multiply(base, base, n)
        b //= 2


    return result

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = matrix_power(matrix, n, b)

for row in result:
    print(" ".join(map(str, row)))
