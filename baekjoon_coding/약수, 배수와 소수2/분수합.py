def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

# 분모의 최소공배수구하기
bot = b * d // gcd(b, d)
top = bot // b * a + bot // d * c

com_divisior=gcd(bot, top)
bot //=com_divisior
top //=com_divisior
print(top, bot)