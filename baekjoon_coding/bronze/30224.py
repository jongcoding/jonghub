number = input().strip()

contains_7 = '7' in number

num_int = int(number)
divisible_by_7 = num_int % 7 == 0

if contains_7 and divisible_by_7:
    print(3)
elif contains_7 and not divisible_by_7:
    print(2)
elif not contains_7 and divisible_by_7:
    print(1)
else:
    print(0)