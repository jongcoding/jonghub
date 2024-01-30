# 불 자료형
# 불 자료형은 어떻게 사용할까?
a = True
b= False
print(type(a))
print(type(b))

print(1==1)
print(2>1)
print(2<1)

# 자료형의 참과 거짓
a=[1,2,3,4]
while a:
    print(a.pop())

if[]:
    print("참")
else:
    print("거짓")

if[1,2,3]:
    print("참")
else:
    print("거짓")

# 불 연산
print(bool('python'))
print(bool(''))

print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(3))
