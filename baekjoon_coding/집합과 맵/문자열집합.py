n,m = map(int, input().split())
list_s=[]
list_search=[]
count=0
for i in range(n):
    list_s.append(input())
set_s=set(list_s)
for j in range(m):
    list_search.append(input())
for word in list_search:
    if word in set_s:
        count+=1
print(count)

    