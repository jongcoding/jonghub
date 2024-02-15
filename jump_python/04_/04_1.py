#04-1 함수
# 함수란 무엇인가?
# 함수를 사용하는 이유는 무엇일까?
# 파이썬 함수의 구조
# def 함수_이름(매개변수):

def add(a, b):
    return a+b

a=3
b=4
c=add(a,b)
print(c)

# 매개 변수와 인수

# 입력값과 리턴값에 따른 함수의 형태
# 일반적인 함수
def add(a, b):
    result= a+b
    return result

a= add(3, 4)
print(a)


# 입력값이 없는 함수
def say():
    return 'HI'
a=say()
print(a)

# 리턴 값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3, 4)
print(add(3,4)) # NONE 리턴 값이 없다는 뜻

# 입력값도 리턴값도 없는 함수
def say():
    print('HI')
say()

# 매개 변수를 지정하여 호출하기
def sub(a, b):
    return a-b

result = sub(a=7, b=3)
print(result)

result= sub(b=5, a=3)
print(result)

# 입력값이 몇 개가 될지 모를 떄는 어떻게 해야 할까?
# 여러 개의 입력 값을 받는 함수 만들기
def add_many(*args):
    result=0
    for i in args:
        result = result+i
    return result

result= add_many(1, 2, 3)
print(result)
result= add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice =="add":
        result=0
        for i in args:
            result=result+i
    elif choice == "mul":
        result =1
        for i in args:
            result = result*i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

# 키워드 매개변수 kewargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

# 함수의 리턴값은 언제나 하나이다.
def add_and_mul(a, b):
    return a+b, a*b

result= add_and_mul(3,4)

result1, result2= add_and_mul(3, 4)

# return의 또 다른 쓰임새
def say_nick(nick):
    if nick =="바보":
        return
    print("나의 별명은 %s입니다." % nick)

say_nick('야호')
say_nick('바보') # return문이 실행되어서 빠져 나옴

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다. " % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박을용" ,27)
say_myself("박을용" ,27, True)
say_myself("박응선", 27, False)

# 함수 안에서 선언한 변수의 효력 버뮈
a= 1
def vartst(a):
    a=a+1

vartst(a)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a= 1 
def vartest(a):
    a= a+1
    return a
a= vartest(a)
print(a)

# 2. global 명령어 사용하기 그다지 좋은 방법은 아니다
a=1
def vartest():
    global a
    a=a+1

vartest()
print(a)

# lambda 예약어
add= lambda a, b: a+b
result= add(3,4)
print(result)