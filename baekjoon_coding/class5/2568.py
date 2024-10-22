import sys
input=sys.stdin.readline
def Lower_Bound(lst, num):
    low = 0
    high = len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        if num <= lst[mid]:
            high = mid
        else:
            low = mid + 1
    return low

dic = {}
lst = []
lis = [-1] 
result = [] 
backtrace = []  

# 입력 받기
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    dic[b] = a

temp = sorted(dic)
for i in temp:
    lst.append(dic[i])

# LIS 구하기
for i in lst:
    if i > lis[-1]:
        lis.append(i)
    else:
        lis[Lower_Bound(lis, i)] = i
    result.append(lis.index(i))  # LIS 길이 저장


lisLength = len(lis) - 1  


for i in range(len(lst) - 1, -1, -1):
    if result[i] == lisLength:
        backtrace.append(lst[i])
        lisLength -= 1

print(n - len(backtrace))

backtrace_set = set(backtrace)
for i in sorted(lst):
    if i not in backtrace_set:
        print(i)
