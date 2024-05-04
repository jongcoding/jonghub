import sys

for line in sys.stdin:
    # 입력을 읽고 각각의 케이스로 분리합니다.
    N, S = map(int, line.split())
    
    # 각 사람당 할당되는 주식의 수를 계산합니다.
    max_shares_per_person = S // (N+1)
    
    # 결과를 출력합니다.
    print(max_shares_per_person)
