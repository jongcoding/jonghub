# 계수정렬
import sys

N = int(sys.stdin.readline().strip())  # 수의 개수 N 입력 받기
count = [0] * 2000001  # 입력되는 수의 범위는 -1,000,000부터 1,000,000까지이므로 총 2,000,001개의 인덱스를 가진 리스트 생성

# 입력된 수의 개수를 카운트
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    count[num + 1000000] += 1

# 정렬된 결과를 출력
for i in range(len(count)):
    if count[i] > 0:
        print(i - 1000000)  # 입력된 수의 범위에 맞게 출력
        count[i] -= 1
