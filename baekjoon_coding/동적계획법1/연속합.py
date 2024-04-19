def find_max(num_list):
    max_ending=max_so_far=num_list[0]
    for x in num_list[1:]:
        max_ending=max(x,max_ending+x)
        max_so_far=max(max_so_far,max_ending)
    return max_so_far
n=int(input())
num_list=list(map(int, input().split()))
max_num=find_max(num_list)
print(max_num)

