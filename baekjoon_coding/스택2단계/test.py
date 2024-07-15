import random

# 1부터 1000까지의 숫자를 리스트로 생성
numbers = list(range(1, 1001))

# 리스트를 무작위로 섞음
random.shuffle(numbers)

# 무작위로 섞인 숫자 출력
for number in numbers:
    print(number)
