import sys
N= int(sys.stdin.readline())
q=list(map(float, sys.stdin.readline().split()))
sum=0.0
max=max(q)
for i in range(N):
    q[i]=q[i]/max*100
    sum= sum+q[i]
print(sum/N)

# 최적화 코드
#import sys

# 입력 받기
#N = int(sys.stdin.readline())
#scores = list(map(float, sys.stdin.readline().split()))

# 최대값 구하기
#max_score = max(scores)

# 각 점수를 조정하고 평균 계산
#adjusted_scores = [(score / max_score) * 100 for score in scores]
#average = sum(adjusted_scores) / N

# 결과 출력
#print(average)