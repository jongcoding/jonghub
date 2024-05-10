import sys
input=sys.stdin.readline
n=int(input().rstrip())
count=0
prev_end_time=0
num_list=[]
for i in range(n):
    num_list.append(list(map(int, input().split())))
num_list.sort(key=lambda x: (x[1], x[0]))
print(num_list)
for start, end in num_list:
    if start >= prev_end_time:
        count+=1
        prev_end_time=end
print(count)
