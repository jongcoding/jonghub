import sys
T= int(sys.stdin.readline())
for i in range(T):
    a, b=map(int, sys.stdin.readline().split())
    sys.stdout.write("Case #%d: %d + %d = %d\n" % (i+1, a, b, a+b))
