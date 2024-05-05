def find_division(num_list, n, m):
    count = 0
    cumulative_sum = [0] * (n + 1)
    
    # 누적 합 계산
    for i in range(1, n + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + num_list[i - 1]
    # 누적 합을 이용하여 부분합 계산 및 m의 배수인지 확인
    remainder_counts = [0] * m
    for i in range(1, n + 1):
        remainder = cumulative_sum[i] % m
        count += remainder_counts[remainder]
        if remainder == 0:
            count += 1
        remainder_counts[remainder] += 1
    
    return count

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

print(find_division(num_list, n, m))
