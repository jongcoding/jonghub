#첫쨰줄에 이동하려는 채널이 주어짐
# 둘쨰줄에 고장난 버튼의수 
# 셋쨰줄에 고장난 버튼

def is_possible_channel(channel, broken_buttons):
    if channel == 0:
        return '0' not in broken_buttons

    while channel > 0:
        if str(channel % 10) in broken_buttons:
            return False
        channel //= 10
    return True

def min_press_count(target, broken_buttons):
    min_press_count = abs(target - 100)  # 초기값 설정: +나 - 버튼만을 이용하여 이동할 경우

    for channel in range(500001):  # 0부터 500000 채널을 검사
        if is_possible_channel(channel, broken_buttons):
            press_count = abs(target - channel) + len(str(channel))  # 버튼 누름 횟수 계산
            min_press_count = min(min_press_count, press_count)

    return min_press_count

# 입력 받기
target_channel = int(input())
broken_button_count = int(input())
if broken_button_count > 0:
    broken_buttons = input().split()
else:
    broken_buttons = []

# 결과 출력
print(min_press_count(target_channel, broken_buttons))
