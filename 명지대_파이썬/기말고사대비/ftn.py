#회원번호가 key, value가 list
member={123456:["abc123", "홍길동", 100000, "6/27 13:00"]}

def login():
    id=input("회원번호를 입력하세요 >> ")
    if not id.isdigit():
        print("회원번호를 숫자를 입력해주세요")
        return 0
    pw=input("비밀번호를 입력하세요 >> ")
    id=int(id)
    if id in member:
        if member[id][0]==pw:
            print(f"{member[id][1]}님 반갑습니다.")
            return id
        else:
            print("로그인이 실패하였습니다.")
            return 0
    else:
        print("로그인이 실패하였습니다.")
        return 0
#회원가입
def register():
    name=input("성함을 입력해 주세요 >> ")
    id = input("회원번호를 입력해 주세요 >>")
    if not id.isdigit():
        print("회원번호를 숫자로 입력해주세요")
        return 0
    id=int(id)
    if id in member:
        print("해당 id가 존재합니다.")
        return 0
    
    pw= input("비밀번호를 입력해 주세요 >> ")
    member[id]=[pw,name, 0, "None"]
    print(f"{name} 회원님 반갑습니다.")
    return id

def schedule(my_id):
    sch=member[my_id][3]
    print(f"다음 일정은 {sch} 입니다")
    alter=input("변경을 원하십니까? (1=일정변경 0=일정유지) >> ")
    if alter=="1":
        date=input("원하시는 일정을 입력해 주세요 >> ")
        member[my_id][3]=date
        print(f"다음 일정이 {member[my_id][3]} 으로 변경되었습니다.")
    elif alter=="0":
        return
    else:
        print("0과 1중에 입력해주세요")
def payment(my_id):
    money=member[my_id][2]
    if money<200000:
        print(f"회비가 {200000-money} 원 부족합니다")
    else:
        print(f"회비잔액이 {money} 원 있습니다.")
    pay=input("얼마를 지불하시겠습니까? >> ")
    if pay.isdigit():
        pay=int(pay)
        member[my_id][2]+=pay
        print(f"남은 회비 잔액은 {member[my_id][2]} 원입니다.")
    else:
        print("입력오류: 숫자를 입력해주세요.")
    
