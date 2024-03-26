n = int(input())  # 계단의 개수
scores = [0] * (n + 1)  # 각 계단에 대한 점수
dp = [0] * (n + 1)  # 동적 계획법을 위한 배열

# 각 계단의 점수 입력
for i in range(1, n + 1):
    scores[i] = int(input())

# 계단의 개수가 1개나 2개인 경우에 대한 처리
if n == 1:
    print(scores[1])
elif n == 2:
    print(scores[1] + scores[2])
else:
    # 첫 번째 계단은 시작점이므로 직접 초기화
    dp[1] = scores[1]

    # 두 번째 계단은 첫 번째 계단을 밟고 올라가는 것이 최대
    dp[2] = scores[1] + scores[2]

    # 세 번째 계단부터 동적 계획법 수행
    for i in range(3, n + 1):
        # i번째 계단을 밟는 경우에는 (i-1번째 계단을 밟지 않았을 때 최대값) + i번째 계단의 점수
        # (i-2번째 계단을 밟지 않았을 때 최대값) + (i-1번째 계단의 점수) + i번째 계단의 점수 중 최대값을 선택
        dp[i] = max(dp[i - 2], dp[i - 3] + scores[i - 1]) + scores[i]

    # 마지막 계단에 도달할 때까지의 최대값 출력
    print(dp[n])