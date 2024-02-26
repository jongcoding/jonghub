a,b=  map(str,input().split())
c=list(a)
e=list(b)
c.reverse()
e.reverse()
f=''.join(map(str,e))
d=''.join(map(str,c))
if int(d)>int(f):
    print(d)
else:
    print(f)

#최적화 코드
#a, b = input().split()

# 두 문자열을 뒤집은 뒤, 정수로 변환하여 비교합니다.
#reversed_a = int(a[::-1])
#reversed_b = int(b[::-1])

# 더 큰 값을 출력합니다.
#print(max(reversed_a, reversed_b))