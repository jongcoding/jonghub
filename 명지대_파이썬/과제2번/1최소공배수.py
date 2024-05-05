# 초기 코인 데이터
lcm = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0:
        if lcm == 0:  # 최소공배수가 아직 설정되지 않았다면
            lcm = i  # 최소공배수를 현재의 i로 설정
        print("3과 7의 공배수 :", i)
print("3과 7의 최소공배수 :", lcm)
