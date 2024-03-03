m=int(input())
n=int(input())
sum=0
start=0
for i in range(m,n+1):
    ll=0
    for j in range(1,i//2+1):
        if i%j==0:
            ll+=1
    if ll==1:
        if start==0:
            start=i
        sum+=i
if sum==0:
    print(-1)
else:
    print(sum)
    print(start)

# 최적화
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

m = int(input())
n = int(input())

sum_of_primes = 0
min_prime = None

for i in range(m, n + 1):
    if is_prime(i):
        sum_of_primes += i
        if min_prime is None:
            min_prime = i

if sum_of_primes == 0:
    print(-1)
else:
    print(sum_of_primes)
    print(min_prime)

