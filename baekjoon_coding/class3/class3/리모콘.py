#첫쨰줄에 이동하려는 채널이 주어짐
# 둘쨰줄에 고장난 버튼의수 
# 셋쨰줄에 고장난 버튼

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


target =int(input())
num=int(input())
if num==0:
    available_digits=list(range(10))
else:
    available_digits =list(set(range(10))-set(map(int, input().split())))


closest = find_closest_number(target, available_digits)
count=abs(target-closest)+len(str(closest))
if abs(target-100)<count:
    count=abs(target-100)
print(count)