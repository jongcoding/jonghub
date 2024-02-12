#03-3 for 문
# for문의 기본 구조
# for 변수 in 리스트(또는 튜플, 문자열): 

# 예제를 통해 for문 이해하기
# 1. 전형적인 for 문
test_list=['one', 'two', 'three']
for i in test_list:
    print(i)

# 2. 다양한 for문의 사용
a=[(1,2), (3,4),(5,6)]
for (first, last) in a:
    print(first+last)

# 3. for문의 응용
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여주시오.
makrs=[90,25,67,45,80]

number=0
for mark in makrs:
    number=number+1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for문과 continue 문
makrs=[90,25,67,45,80]

number=0
for mark in makrs:
    number=number+1
    if mark <=60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# for문과 함꼐 자주 사용하는 range 함수
a=range(10)
print(a)
a=range(1,11)
print(a)

# range 함수의 예시 살펴보기
add=0
for i in range(1,11):
    add=add+i

print(add)

makrs=[90,25,67,45,80]

for num in range(len(makrs)):
    if makrs[num] <60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (num +1))

# 1분 코딩 for문과 range 함수를 사용하여 1부터 100까지 더해 보자.
add=0
for i in range(1, 100):
    add=add+i
print(add)

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end= " ")
    print('')

#  라스트 컴프리헨션 사용하기
a= [1,2,3,4]
result= []
for num in a:
    result.append(num*3)

print(result)

result=[]
result = [num*3 for num in a]
print(result)

result=[]
result=[num*3 for num in a if num%2 ==0]
print(result)