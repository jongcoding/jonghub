num_list=[int(input()) for _ in range(5)]
sum=0
for i in range(5):
    sum+=num_list[i]
num_list.sort()
print(int(sum/5))
print(num_list[2])