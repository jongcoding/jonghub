n=int(input())
# 공식 n= 5*a+3*b
a=n//5
b=(n-5*a)//3
num_list=[]
while True:
    if n==5*a+3*b and a>-1:
        num_list.append(a+b)
        break
    else:
        if a==-1 and num_list==[]:
            num_list.append(-1)
            break
    a-=1
    imp=n-a*5
    b=imp//3
print(num_list[0])