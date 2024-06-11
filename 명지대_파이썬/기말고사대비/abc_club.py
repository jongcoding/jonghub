import ftn as ftn
print("파이썬 기말고사 제 이름은 홍길동 학번은 123456 입니다")
print("==================================================")
my_id=0
while True:
    cmd=input("ABC 수영클럽 (1=로그인 2=회원가입 3=일정 4=회비 0=종료) >> ")
    if cmd.isdigit():
        cmd=int(cmd)    
    if cmd==1:
        my_id=ftn.login()
    elif cmd==2:
        my_id=ftn.register()
    elif cmd==3:
        if my_id==0:
            print("먼저 로그인을 해주세요")
        else:
            ftn.schedule(my_id)
    elif cmd==4:
        if my_id==0:
            print("먼저 로그인을 해주세요")
        else:
            ftn.payment(my_id)
    elif cmd ==0:
        print("감사합니다")
        break
    else:
        print("잘못된 명령입니다. 다시 입력해주세요")
    print()