n= int(input())
people_list=set()
for _ in range(n):
    a,b= input().split()
    if b=="enter":
        people_list.add(a)
    elif b=="leave":
        people_list.remove(a)

for people in sorted(people_list, reverse=True):
    print(people) 