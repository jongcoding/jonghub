i=[a for a in map(int,input().split())]
a=0
b=0
for j in range(8):
    if j+1 ==i[j]:
        a+=1
    elif j+1==i[7-j]:
        b+=1
if a==8:
    print("ascending")
elif b==8:
    print("descending")
else:
    print("mixed")

# 최적화 코드 
# 입력 받기
numbers = [int(x) for x in input().split()]

# 오름차순인지 확인
if numbers == sorted(numbers):
    print("ascending")
# 내림차순인지 확인
elif numbers == sorted(numbers, reverse=True):
    print("descending")
# 혼합된 숫자
else:
    print("mixed")