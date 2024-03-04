list_x=[]
list_y=[]
for _ in range(int(input())):
    a,b= map(int,input().split())
    list_x.append(a)
    list_y.append(b)
print((max(list_x)-min(list_x))*(max(list_y)-min(list_y)))