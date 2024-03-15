s = input()  # 문자열을 입력으로 받음
s_list = set()  # 중복을 제거하기 위한 set 생성

# 부분 문자열 생성 및 중복 제거
for i in range(1, len(s) + 1):  # 부분 문자열의 길이를 1부터 문자열의 전체 길이까지 순회
    for j in range(len(s) - i + 1):  # 문자열 길이에 따른 부분 문자열 생성을 위한 루프
        new_substring = s[j:j+i]  # 현재 부분 문자열 추출
        s_list.add(new_substring)  # 중복을 제거하기 위해 set에 추가

print(len(s_list))  # 중복이 제거된 부분 문자열의 개수 출력
