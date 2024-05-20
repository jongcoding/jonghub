p = 1000000007

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res = (res * i)
    return res

def power(x, y):
    res = 1
    x = x % p
    while y > 0:
        if y % 2:
            res = (res * x)%p 
        y = y // 2
        x = pow(x,2,p)
    return res

def mod_inverse(x):
    return power(x, p-2)

def comb(n, k):
    if k > n:
        return 0
    numerator = factorial(n)
    denominator = (factorial(k) * factorial(n - k))
    return (numerator * mod_inverse(denominator))%p

n, k = map(int, input().split())
print(comb(n, k))