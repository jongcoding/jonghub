N = int(input())

# base는 현재 검사 중인 수를 나타내는 변수
base = 666

# count는 종말의 수를 세는 변수
count = 0

while True:
    # 만약 현재 수에 '666'이 포함되어 있다면
    if '666' in str(base):
        count += 1  # count를 1 증가시킴
        # 만약 count가 N과 같아지면 종료
        if count == N:
            print(base)
            break

    # 다음 수로 넘어감
    base += 1
