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