from itertools import permutations

n,m = map(int, input().split())

new_list=list(map(int, input().split()))
all= list(permutations(new_list,m))
all.sort()
for i in all:
    for j in i:
        print(j, end=" ")
    print()