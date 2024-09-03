import sys
input=sys.stdin.readline
n=int(input().rstrip())
car=list(map(int, input().rstrip().split()))
count=0
for c in car:
    if c==n:
        count+=1
print(count)