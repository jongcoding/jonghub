import sys
input=sys.stdin.readline
n=int(input())
chong_list={'ChongChong'}
count=1
for _ in range(n):
    a,b= input().rstrip().split()
    if (a in chong_list) and (b not in chong_list):
       count+=1 
       chong_list.add(b)
    elif (b in chong_list) and (a not in chong_list):
        count+=1
        chong_list.add(a)
print(count)