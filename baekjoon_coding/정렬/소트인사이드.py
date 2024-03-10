n=str(input())
num=list(n)
num.sort()
num.reverse()
st1=""
for i in range(len(num)):
    if i==len(num):
        print(num[i])
    else:
        print(num[i],end="")


