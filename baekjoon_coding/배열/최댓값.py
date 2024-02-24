import sys
q=[]
for i in range(9):
    q.append(int(sys.stdin.readline()))
print(max(q))
print(q.index(max(q))+1)