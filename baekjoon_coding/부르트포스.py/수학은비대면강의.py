a,b,c,d,e,f=map(int, input().split())
x=(c*e-f*b)//(a*e-b*d)
y=(c*d-a*f)//(b*d-a*e)
print(x,y)