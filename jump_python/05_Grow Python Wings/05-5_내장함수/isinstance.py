# 첫 번째 인수로 객체, 두 번째 인수로 클래스를 받는다.
# 입력 받은 객체가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 리턴
class Person: pass
a=Person()
print(isinstance(a, Person))
b=3
print(isinstance(b, Person))
