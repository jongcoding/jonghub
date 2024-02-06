#if 문
money =True
if money:
    print("택시를 타고가라")
else:
    print("걸어가라")

# 들여쓰기 방법 알아보기
money =True
if money:
    print("택시를")
    print("타고")
    print("걸어가라")

# 조건문이 무엇인가?

# 비교 연산자
x=3
y=2
print(x>y)

money =2000
if money >= 3000:
    print("택시를 타고가라")
else:
    print("걸어거라")

# and, or, not
money= 2000
card= True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어거라")

# in, not in
1 in [1,2,3]
1 not in [1,2,3]

print('a' in ('a','b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고가라")
else:
    print("걸어가라")

# 조건문에서 아무일도 하지 않게 설정하고 싶다면?
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어가라")

# 다양한 조건을 판단하는 elif
pocket = ['paper', 'cellphone']
card= True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
        print("택시를 타고가라")
else:
        print("걸어가라")

# if 문을 한 줄로 작성하기
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: pass
else: print("걸어가라")

# 조건부 표현식
score=30
if score>= 60:
    message="success"
else:
    message="failure"

message="succes" if score >= 60 else "failure"