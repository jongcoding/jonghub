data=[]
best=0
while True:
    try:
        a=list(map(str,input()))
        data.append(a)
        if best<len(a):
            best=len(a)
    except EOFError:
        for i in range(best):
            for j in range(len(data)):
                if len(data[j])>i:
                    print(data[j][i],end="")
                else:
                    pass
        break

# 최적화 코드
data = []
max_length = 0

# 입력 받기
while True:
    try:
        line = list(input())
        data.append(line)
        max_length = max(max_length, len(line))
    except EOFError:
        break

# 출력
for i in range(max_length):
    for line in data:
        if i < len(line):
            print(line[i], end="")
    print()  # 다음 행으로 이동