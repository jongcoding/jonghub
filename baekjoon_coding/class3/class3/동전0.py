from collections import deque
n,k=map(int, input().split())
coin=deque([])

coin_count=0
for _ in range(n):
    a=int(input())
    coin.appendleft(a)
reversed(coin)
for num in coin:
    coin_count+=k//num
    k=k%num
print(coin_count)

