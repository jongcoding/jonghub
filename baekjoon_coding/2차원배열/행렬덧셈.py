n,m=map(int,input().split())
data=[[],[]]
for i in range(2):
    for j in range(n):
        a=list(map(int, input().split()))
        data[i].append(a)
        if i==1:
            for k in range(m):
                data[0][j][k]+= data[1][j][k]
del(data[1])
for i in range(n):
    print(" ".join(map(str, data[0][i])))      

# 최적화 코드
n, m = map(int, input().split())

# 두 개의 2차원 배열을 하나로 합치기
data = []
for _ in range(n * 2):
    data.append(list(map(int, input().split())))

# 각 위치의 값을 더하기
for i in range(n):
    for j in range(m):
        data[i][j] += data[i + n][j]

# 결과 출력
for row in data[:n]:
    print(" ".join(map(str, row)))