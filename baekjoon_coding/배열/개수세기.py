import sys
N= int(sys.stdin.readline())
Q=list(map(int, sys.stdin.readline().split()))
v=int(sys.stdin.readline())
count=Q.count(v)
sys.stdout.write(str(count))
