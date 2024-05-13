# 알파벳을 입력 받습니다.
char = input()

# 입력된 알파벳이 'N' 또는 'n'이면 "Naver D2"를 출력하고, 그 외의 경우에는 "Naver Whale"를 출력합니다.
if char.lower() == 'n':
    print("Naver D2")
else:
    print("Naver Whale")
