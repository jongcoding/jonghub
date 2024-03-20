N = int(input())
people = []

# 사람들의 정보를 입력 받음
for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

# 각 사람의 덩치 등수 계산
ranks = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)

# 덩치 등수 출력
print(*ranks)