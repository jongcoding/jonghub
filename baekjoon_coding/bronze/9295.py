import sys 
input=sys.stdin.readline
t=int(input().rstrip())
for i in range(1, t+1):
    a,b=map(int, input().rstrip().split())
    print(f"Case {i}: {a+b}")