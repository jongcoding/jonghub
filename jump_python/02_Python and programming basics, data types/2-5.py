#딕셔너리 자료형

dic ={'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

print(type(dic))

a= {1: 'hi'}
b= {'a': [1, 2, 3]}

# 딕셔너리 쌍 추가
a[2] ='b'
print(a)
a['name']= 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)

#딕셔너리 요소 삭제하기
del a[1]
print(a)

#딕셔너리 사용하는 방법

# 딕셔너리에서 key를 사용해 value 얻기
grade= {'pey': 10, 'julliet':99}
print(grade['pey'])
print(grade['julliet'])

a= {1: 'a', 2: 'b'}
print(a[1])
print(a[2])

a= {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])

dic= {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

#딕셔너리 만들 때 주의할 사항
a= {1: 'a', 1: 'b'} # 1이라는 key 값이 중복으로 사용
print(a)  # 1:'a' 쌍이 무시됨.

# a={[1,2]: 'hi'} #error - 리스트를 key로 사용함

# 딕셔너리 관련 함수
dic= {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic.keys())


for k in dic.keys():
    print(k)

print(list(dic.keys()))

# value 리스트 만들기
print(dic.values())

#key. value 쌍 얻기 items
print(dic.items())

#key value 쌍 모두 지우기- clear
print(dic.clear())

#key로 value 얻기 - get
dic= {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic.get('name'))
print(dic.get('phone'))
print(dic.get('nokey'))
# print(dic['nokey'])

print(dic.get('nokey', 'foo'))

#해당 key가 딕셔너리 안에 있는지 조사하기 - in
print('name' in dic)
print('email' in a)

#1분 코딩
dic={'name': '홍길동', 'birth': '1128', 'age': 30}
print(dic)