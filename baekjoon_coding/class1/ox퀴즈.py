n=int(input())

for i in range(n):
    q=0
    num=0
    quiz=list(input())
    for j in range(len(quiz)):
        if quiz[j]=="O":
            q+=1
            num+=q
        else:
            q=0
    print(num)

# 최적화 코드
n = int(input())

for _ in range(n):
    total_score = 0
    consecutive_score = 0
    quiz_results = input()

    for index, result in enumerate(quiz_results):
        if result == "O":
            consecutive_score += 1
            total_score += consecutive_score
        else:
            consecutive_score = 0

    print(total_score)