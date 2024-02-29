num=int(input())
for _ in range(num):
    h,w,n=map(int,input().split())
    H=0
    W=1
    for N in range(n):
        H+=100
        if H>h*100:
            W+=1
            H=100
    print(H+W)
#최적화 코드
num = int(input())

for _ in range(num):
    h, w, n = map(int, input().split())

    # 호수 계산
    floor = n % h if n % h != 0 else h
    room = n // h if n % h == 0 else n // h + 1

    # 출력
    print(floor * 100 + room)