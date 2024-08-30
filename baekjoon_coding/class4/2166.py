import sys
input=sys.stdin.readline
def area(n, points):
    sum=0
    for i in range(n):
        x1,y1=points[i]
        x2,y2=points[(i+1)%n]
        sum+=(x1*y2-x2*y1)
    return abs(sum/2)

n=int(input().rstrip())
points=[]
for _ in range(n):
    points.append(tuple(map(float, input().rstrip().split())))

print(f"{area(n,points):.1f}")