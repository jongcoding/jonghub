t1=()
t2= (1, )
t3= (1,2,3)
t4= 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(t5)
# del 불가능 튜플은 변경 불가능

# 인덱싱하기
print(t5[0])

#슬라이싱하기
print(t5[1:])

#튜플 더하기
t6= t3+t5
print(t6)

#튜플 곱하기
t7= t3*3
print(t7)

#튜플 길이 구하기
print(len(t5))
