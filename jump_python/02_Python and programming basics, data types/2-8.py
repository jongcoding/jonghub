# 자료형의 값을 저장하는 공간, 변수
# 변수는 어떻게 만들까?
a=1
b="python"
c=[1,2,3]
# 변수_이름= 변수에_저장할_값

#변수란?
a=[1,2,3]
print(id(a))

#리스트를 복사하고자 할 때
a=[1,2,3]
b=a
print(id(a))
print(id(b))
print(a is b)
a[1]=4
print(a)
print(b)

# 1. [:] 이용하기
a=[1,2,3]
b= a[:]
a[1]=4
print(a)
print(b)
# 2. copy 모듈 이용하기
from copy import copy
a=[1,2,3]
b=copy(a)
print(b is a)

# copy 함수 이용하기
a=[1,2,3]
b=a.copy()
print(b is a)

# 변수를 만드는 여러가지 방법
(a,b)='python', 'life'
[a,b]=['python', 'life']

a=b='python'

a=3
b=5
a,b=b,a
print(a)
print(b)
