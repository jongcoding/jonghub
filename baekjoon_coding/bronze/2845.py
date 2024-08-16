l,p=map(int, input().split())
people=list(map(int, input().split()))
total=l*p
for p in people:
    print(p-total,end=" ")