def cantor_set(N, start, end, start_y, end_y, line):
   
    if N==1:
        return line
    for j in range(start_y, end_y):
        for i in range(start, end):
            line[j][i] = ' '
    num=N//3
    cantor_set(num, start-num//3*2, start-num//3, start_y+num//3, start_y+num//3*2,line)
    cantor_set(num, end+num//3, end+num//3*2, start_y+num//3, start_y+num//3*2, line)
    cantor_set(num, end+num//3, end+num//3*2, end_y+num//3, end_y+num//3*2, line)
    cantor_set(num, end+num//3, end+num//3*2, start_y-num//3*2, start_y-num//3, line)
    cantor_set(num, start-num//3*2, start-num//3, start_y-num//3*2, start_y-num//3, line)
    cantor_set(num, end-num//3*2, end-num//3, end_y+num//3, end_y+num//3*2, line)
    cantor_set(num, start-num//3*2, start-num//3, end_y+num//3, end_y+num//3*2, line)
    cantor_set(num, end-num//3*2, end-num//3, start_y-num//3*2, start_y-num//3, line)
# 입력 처리

N = int(input().strip())
start = N//3
end = N//3*2
start_y= N//3
end_y = N//3*2
line = [['*']*N for _ in range(N)] 
# 칸토어 집합 생성 후 출력
cantor_set(N, start, end, start_y, end_y,line)
for j in range(N):
    print(''.join(line[j]))