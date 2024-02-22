X=int(input())
N=int(input())
t=0
for _ in range(N):
    a,b = map(int, input().split())
    t+=a*b
if X == t:
    print("Yes")
else:
    print("No")