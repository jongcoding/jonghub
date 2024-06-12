import mySmartBook as msb
print("이종윤(학번 60201970)의 스마트 가게부에 오신 것을 환영합니다")
while True:
    cmd=input("명령을 입력하세요. 1=수입 2=지출 3=출력 4=계산기 q=종료 >> ")
    if cmd =="1":
        msb.income()
    elif cmd =="2":
        msb.expense()
    elif cmd =="3":
        msb.show()
    elif cmd =="4":
        msb.calc()
    elif cmd =="q":
        print("이용해 주셔서 감사합니다")
        break    
    else:
        print("잘못된 명령입니다. 다시 입력해주세요.")