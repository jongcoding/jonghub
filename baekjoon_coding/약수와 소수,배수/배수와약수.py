# 약수라면 factor
# 배수라면 multiple
# 둘다아니라면 neither
while True:
    a,b= map(int, input().split())
    if a==0 and b==0:
        break
    if b%a==0:
        print("factor")
    elif a%b==0:
        print("multiple")
    else:
        print("neither")


# 0 0이면 출력 종료
