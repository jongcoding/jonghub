def find_closest_number(target):
    closest_number = 0

    # 각 자릿수별로 주어진 범위 내에서 가장 가까운 숫자 찾기
    digits = [int(d) for d in str(target)]
    for i, digit in enumerate(digits):
        closest_number += min(digit, 6) * (10 ** (len(digits) - 1 - i))

    if digits[-1] < 6:  # 일의 자리 수가 6보다 작으면 0으로 변경
        closest_number -= digits[-1]
    else:  # 일의 자리 수가 6보다 크거나 같으면 10으로 변경
        closest_number += 10 - digits[-1]

    return closest_number

# 예시: 특정 숫자 659에 가장 가까운 숫자 찾기
target = 659
closest = find_closest_number(target)
print("특정 숫자에 가장 가까운 숫자:", closest)