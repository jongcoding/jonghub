p = 1000000007

def matrix_mult(A, B, p):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % p, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % p],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % p, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % p]]

def f_pow(n):
    if n == 1:
        return [[1, 1], [1, 0]]
    else:
        t = f_pow(n // 2)
        t2 = matrix_mult(t, t, p)
        if n % 2 == 1:
            t2 = matrix_mult(t2, [[1, 1], [1, 0]], p)
        return t2

n = int(input())

if n == 0:
    print(0)
else:
    t = f_pow(n)
    print(t[0][1])
