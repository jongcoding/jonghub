n= int(input())
x_y=list(map(int ,input().split()))
sorted_x_y=sorted(list(set(x_y))) # 중복 값제거 및 정렬
direct={sorted_x_y[i]: i for i in range(len(sorted_x_y))}
result=[direct[num] for num in x_y]
print(*result)