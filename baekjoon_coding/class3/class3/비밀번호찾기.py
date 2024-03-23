import sys
n,m =map(int,sys.stdin.readline().rstrip().split())
site_pass=dict()
for i in range(n):
    a,b=sys.stdin.readline().rstrip().split()
    site_pass[a]=b
for _ in range(m):
    print(site_pass[sys.stdin.readline().rstrip()])
