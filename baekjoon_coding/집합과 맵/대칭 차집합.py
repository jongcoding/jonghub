n,m=map(int, input().split())
a_list=set(map(int, input().split()))
b_list=set(map(int, input().split()))
c_list=a_list-b_list
d_list=b_list-a_list
print(len(c_list)+len(d_list))
