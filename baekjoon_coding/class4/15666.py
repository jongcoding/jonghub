from itertools import combinations_with_replacement

n,m = map(int, input().split())
new_list=list(map(int, input().split()))
new_list.sort()
resullt=list(set(combinations_with_replacement(new_list,m)))
resullt.sort()
for i in resullt:
    for j in i:
        print(j, end=" ")
    print()