# 사용자 입출력

# 사용자 입력 활용하기
# input 사용하기
a= input()
print(a)

# 프롬프트를 띄워 사용자 입력 받기
number= input("숫자를 입력하세요: ")
print(number)

#print 자세히 알기

# 큰 따옴표로 둘러싸인 문자열은 +연산과 동일하다.
print("life" "is" "too short")
print("life" +"is"+"too short")

# 문자열 띄어쓰기는 쉼표로 한다.
print("life", "is", "too short")

# 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end= ' ')