# 함수 정의: 칸토어 집합 생성
def cantor_set(N, start, end, line):
    if N==1:
        return line
    for i in range(start, end):
        line[i] = ' '
    num=N//3
    cantor_set(num, start-num//3*2, start-num//3, line)
    cantor_set(num, end+num//3, end+num//3*2, line)
# 입력 처리
try:
    while True:
            N = int(input().strip())
            N = 3 ** N
            start = N//3
            end = N//3*2
            line = ['-'] * N
            # 칸토어 집합 생성 후 출력
            cantor_set(N, start, end, line)
            print(''.join(line))
except:
     exit()