
a, b= map(int, input().split())
li=[]
while True:
    if a%b >=10:
        li.append(chr(a%b+55))
    elif a% b <10:
        li.append(a%b)
    a=a//b
    if a==0:
        li.reverse()
        print("".join(map(str,li)))
        break

# 최적화 코드
def convert_base(a, b):
    # 10진수를 b진수로 변환하는 함수
    result = []
    while a > 0:
        remainder = a % b
        if remainder >= 10:
            result.append(chr(remainder + 55))
        else:
            result.append(str(remainder))
        a //= b
    return ''.join(result[::-1])

# 입력
a, b = map(int, input().split())

# 결과 출력
print(convert_base(a, b))
