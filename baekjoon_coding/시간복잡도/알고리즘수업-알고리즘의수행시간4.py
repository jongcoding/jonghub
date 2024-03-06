n = int(input())

# 코드1의 수행 횟수 계산
execution_count = 0
for i in range(1, n):
    for j in range(i + 1, n + 1):
        execution_count += 1
print(execution_count)

# 다항식으로 나타내었을 때의 최고차항의 차수 계산
if execution_count <= 3:
    polynomial_degree = execution_count
else:
    polynomial_degree = 4
print(polynomial_degree)
