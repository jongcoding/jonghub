s1=set([])
for _ in range(1, 11):
    number=int(input())
    s1.add(number%42)
print(len(s1))
# 최적화 코드
# print(len(set([int(input())%42 for _ in range(10)])))