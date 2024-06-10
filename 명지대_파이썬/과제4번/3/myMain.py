import mySmartBook as mt
print("이종윤(학번 60201970)의 스마트 가계부에 오신 것을 환영합니다")

while True:
    cmd=input("명령 입력: 1=수입 2=지출 3=출력 4=계산기 q=종료 >> ")
    if cmd=='1':
        mt.income()
    elif cmd =='2':
        mt.expense()
    elif cmd =='3':
        mt.show()
    elif cmd =='4':
        mt.calc()
    elif cmd =='q':
        print("이용해 주셔서 감사합니다")
        break
    else:
        print("잘못된 명령입니다. 1, 2, 3, 4, q 중에서 명령을 입력하세요")
