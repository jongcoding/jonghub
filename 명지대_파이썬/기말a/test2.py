import test as hi
while True:
    cmd=input("명령을 입력하세요:")
    if cmd=="1":
        hi.show()
    elif cmd =="2":
        hi.myLotto()
    elif cmd=="3":
        expression=input("계산식을 넣어주세요")
        hi.myCalc(expression)
    elif cmd=="4":
        movie=int(input("영화번호를 적으세요:"))
        ticket=int(input("구매할 티켓 장수를 적으세요:"))
        hi.myMovie(movie, ticket)
        hi.show()
    elif cmd=="q":
        print("종료합니다")
        break