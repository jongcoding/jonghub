import datetime
my_money_book={'점심': ('2022년 6월 8일 10시 30분', '지출', '외식', 10000, '파스타 신용카드 사용')}

# 날짜 
def my_date():
    crt=datetime.datetime.now()
    return str(f"{crt.year}년 {crt.month}월 {crt.day}일 {crt.hour}시 {crt.minute}분")

# 오류 여부 확인 
def check(cmd):
    if not len(cmd)==4:
        print("잘못된 명령입니다. 다시 입력해주세요")
        return False
    if not cmd[2].isdigit():
        print("잘못된 명령입니다. 금액을 숫자로 적어주세요")
        return False
    if cmd[0] in my_money_book:
            print("해당 항목이 이미 존재합니다. 항목명을 변경해주세요.")
            return False
    return True

# 수입
def income():
    inc=input("수입을 입력해 주세요 (예: 5월급여 월급 2000000 까페알바) >> ").split()
    if check(inc):
        my_money_book[inc[0]]=(my_date(),"수입", inc[1],int(inc[2]),inc[3])
    
# 지출
def expense():
    exp=input("지출을 입력해 주세요 (예: 저녁 외식 30000 중국집) >> ").split()
    if check(exp):
        my_money_book[exp[0]]=(my_date(),"지출", exp[1],int(exp[2]),exp[3])
# SHOW    
def show():
    income=0
    expense=0
    for key, value in my_money_book.items():
        print(f"{value[0]} - {key}: [{value[1]}] 그룹={value[2]}, 금액={value[3]}원, 메모={value[4]}")
        if value[1]=="지출":
            expense+=value[3]
        else:
            income+=value[3]
    print(f"총 수입 {income}원, 총지출 {expense}원 수입-지출={income-expense}원")
# 계산기
# EVAL 함수의 취약점 떄문에 보안적 코드를 짜봄
def calc():
    def is_valid_char(c):
        return c.isdigit() or c in "+-*/().% "

    order = input("계산식을 입력하세요 (예: 2000*(3000+25000)/100) >> ")
    
    if all(is_valid_char(c) for c in order):
        try:
            result = eval(order)
            print(f'계산 결과는 {result} 입니다.')
            my_money_book['계산기'] = (my_date(), '계산기', '계산기', 0, str(f"{order} = {result}"))
        except (SyntaxError, NameError):
            print("잘못된 입력입니다. 올바른 계산식을 입력해주세요.")
    else:
        print("잘못된 입력입니다. 올바른 계산식을 입력해주세요.")
