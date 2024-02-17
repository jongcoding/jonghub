# 파일 읽고 쓰기
# 파일 생성하기
f = open("새파일.txt", 'w')
f.close()

# r: 읽기모드, w: 쓰기모드, a: 추가모드
f= open("C:/Users/ialle/OneDrive - 명지대학교/바탕 화면/coding/jonghub/jump_python/04_/새파일.txt", 'w')
f.close()

#파일을 쓰기 모드로 열어 내용쓰기
f= open("C:/Users/ialle/OneDrive - 명지대학교/바탕 화면/coding/jonghub/jump_python/04_/새파일.txt", 'w')
for i in range(1, 11):
    data= "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#파일을 읽는 여러 가지 방법
# readline 함수 이용하기
f= open("C:/Users/ialle/OneDrive - 명지대학교/바탕 화면/coding/jonghub/jump_python/04_/새파일.txt", 'r')
line= f.readline()
print(line)
f.close()

f= open("C:/Users/ialle/OneDrive - 명지대학교/바탕 화면/coding/jonghub/jump_python/04_/새파일.txt", 'r')
while True:
    line= f.readline()
    if not line:break
    print(line)
f.close()

#readlines 함수 사용하기
f= open("C:/Users/ialle/OneDrive - 명지대학교/바탕 화면/coding/jonghub/jump_python/04_/새파일.txt", 'r')
lines= f.readlines()
for line in lines:
    print(line)
f.close()

# 줄 바꿈\n 문자 제거하기
f= open("C:/Users/ialle/OneDrive - 명지대학교/바탕 화면/coding/jonghub/jump_python/04_/새파일.txt", 'r')
lines= f.readlines()
for line in lines:
    line=line.strip() # 줄 끝의 줄바꿈 문자 제거
    print(line)
f.close()

# read 함수 사용하기 -> 파일 내용전체를 문자열로 리턴
f= open("C:/Users/ialle/OneDrive - 명지대학교/바탕 화면/coding/jonghub/jump_python/04_/새파일.txt", 'r')
data=f.read()
print(data)
f.close()

# 파일 객체를 for 문과 함께 사용하기
f= open("C:/Users/ialle/OneDrive - 명지대학교/바탕 화면/coding/jonghub/jump_python/04_/새파일.txt", 'r')
for line in f:
    print(line)
f.close()

#파일에 새로운 내용추가하기
f= open("C:/Users/ialle/OneDrive - 명지대학교/바탕 화면/coding/jonghub/jump_python/04_/새파일.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with 문과 함께 사용하기
f= open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")