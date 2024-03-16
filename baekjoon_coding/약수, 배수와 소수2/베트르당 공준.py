# 에라토스테네스의 체 알고리즘을 사용하여 주어진 범위 내에서 소수를 한 번에 확인
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]

primes_up_to_2n = sieve_of_eratosthenes(2 * 123456)

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for prime in primes_up_to_2n:
        if n < prime <= 2 * n:
            count += 1
    print(count)