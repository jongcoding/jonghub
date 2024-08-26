import sys
input=sys.stdin.readline
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
s=[a,b,c]
p=min(s)
q=min(d,e)
print(p+q-50)