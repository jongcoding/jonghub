import sys
input=sys.stdin.readline
n=int(input().rstrip())
count=0
appence=-1
peoplechat=set()
for _ in range(n):
    gomgom=input().rstrip()
    if gomgom=="ENTER":
        peoplechat=set()
    else:
        if gomgom not in peoplechat:
            peoplechat.add(gomgom)
            count+=1
print(count)