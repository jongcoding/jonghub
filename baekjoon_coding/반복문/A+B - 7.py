T= int(input())
F=[]
for i in range(T):
    F.append(sum(map(int, input().split())))
for i in range(T):
    print("Case #%d: %d" % (i+1, F[i]))

import sys

