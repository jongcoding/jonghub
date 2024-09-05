import sys
input=sys.stdin.readline
while True:
    m,f=map(int, input().split())
    if m==0 and f==0:
        exit()
    print(m+f)