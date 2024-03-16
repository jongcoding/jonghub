def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

case=int(input())

for _ in range(case):
    n= int(input())
    
    while True:
        if is_prime(n):
            print(n)
            break
        else: 
            n+=1

