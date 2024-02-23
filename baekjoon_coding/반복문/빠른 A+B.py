import sys
T= int(sys.stdin.readline())
C=[]
for _ in range(T):
    C.append(sum(map(int, sys.stdin.readline().split())))
sys.stdout.write('\n'.join(map(str, C)))