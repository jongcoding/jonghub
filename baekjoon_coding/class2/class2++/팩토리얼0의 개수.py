import math
n=int(input())
num=math.factorial(n)
num_list=list(str(num))
num_list.reverse()
count=0
for number in num_list:
    if number=='0':
        count+=1
    else:
        break 
print(count)