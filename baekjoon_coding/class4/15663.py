from itertools import permutations

n,m = map(int, input().split())
new_list=list(map(int, input().split()))
resullt=list(set(permutations(new_list,m)))
resullt.sort()
for i in resullt:
    for j in i:
        print(j, end=" ")
    print()
