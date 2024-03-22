from itertools import product

def find_closest_number(target, available_digits):
    closest_number = None
    min_difference = float('inf')

    # 가능한 숫자 조합 생성
    for digits in product(available_digits, repeat=len(str(target))):
        number = int(''.join(map(str, digits)))

        # 주어진 숫자와의 차이 계산
        difference = abs(number - target)

        # 가장 작은 차이를 가진 숫자 선택
        if difference < min_difference:
            min_difference = difference
            closest_number = number

    return closest_number

# 가능한 숫자: 1, 3, 5
available_digits = [1, 3, 5]
target = 554

closest = find_closest_number(target, available_digits)
print("특정 숫자에 가장 가까운 숫자:", closest)  # 출력: 555
