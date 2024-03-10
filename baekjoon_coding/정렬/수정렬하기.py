n=int(input())
num_list=[int(input()) for _ in range(n)]
for i in range(n):
    num_list.sort()
    print(num_list[i])