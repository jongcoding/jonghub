num_x=[]
num_y=[]
for _ in range(3):
    a, b= map(int, input().split())
    num_x.append(a)
    num_y.append(b)
num_x.sort()
num_y.sort()
if num_x.count(num_x[0])>num_x.count(num_x[2]):
    print(num_x[2],end=" ")
else:
    print(num_x[0],end=" ")
if num_y.count(num_y[0])>num_y.count(num_y[2]):
    print(num_y[2])
else:
    print(num_y[0])



