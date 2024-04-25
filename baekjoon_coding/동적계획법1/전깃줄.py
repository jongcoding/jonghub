# 전기줄을 교차하지 않음
# 모든 전깃줄이 서로 교차하지않게 하기 위해 없애야 하는 젓깃줄 최소개수

def inc_sub_seq(n, num_list):
    dp=[[] for _ in range(n)]
    dp[0]=[num_list[0]]
    max_count=1
    for i in range(1, n):
        max_sub_seq = []  # i번째 요소를 끝으로 하는 가장 긴 부분 수열을 저장할 변수
        for j in range(i):
            if num_list[j] < num_list[i] and len(dp[j]) > len(max_sub_seq):
                max_sub_seq = dp[j].copy()  # j번째 요소까지의 부분 수열을 복사
        dp[i] = max_sub_seq + [num_list[i]]
        if max_count<len(dp[i]):
            max_count=len(dp[i])  # 현재 요소를 부분 수열에 추가
    print(n-max_count)
n=int(input())
connections = [tuple(map(int, input().split())) for _ in range(n)]
connections.sort()
B_positions = [b for _, b in connections]

inc_sub_seq(n, B_positions)

