import datetime
my_money_book={'점심':('2022년 6월 8일 10시 30분', '지출', '외식',10000, '파스타 신용카드 사용')}
def my_date():
    crt=datetime.datetime.now()
    array=f"{crt.year}년 {crt.month}월 {crt.day}일 {crt.hour}시 {crt.minute}분"
    return array

# 1,2번 명령 오류 여부 확인
def check(order):
        if not len(order)==4:
            print("잘못된 입력입니다. '항목 그룹 금액 메모' 항목을 입력해주세요")
            return False
        if not order[2].isdigit():
            print("잘못된 입력입니다. 금액을 숫자로 입력해주셔야합니다.")
            return False
        if order[0] in my_money_book:
            print("해당 항목이 이미 존재합니다. 항목명을 변경해주세요.")
            return False
        return True

# 수입 명령
def income():
    order=list(input("수입을 입력해 주세요 (예: 5월급여 월급 2000000 까페알바) >> ").split())
    if check(order):
        my_money_book[order[0]]=(my_date(),'수입', order[1], order[2],order[3])

# 지출 명령
def expense():
    order=list(input("지출을 입력해 주세요 (예: 저녁 외식 30000 중국집) >>").split())
    if check(order):
        my_money_book[order[0]]=(my_date(),'지출', order[1], order[2],order[3])

# 출력 명령
def show():
    plus=0
    minus=0
    for key, value in my_money_book.items():
        print(f'{value[0]} - {key}: [{value[1]}] 그룹={value[2]}, 금액={value[3]}, 메모={value[4]}')
        if value[1]=='지출':
            minus+=int(value[3])
        else:
            plus+=int(value[3])
    total=plus-minus
    print(f"총수입 {plus}원, 총지출 {minus}원 수입-지출={total}원")

# 계산기 명령
def calc():
    def is_valid_char(c):
        return c.isdigit() or c in "+-*/().% "

    order = input("계산식을 입력하세요 (예: 2000*(3000+25000)/100) >> ")
    
    if all(is_valid_char(c) for c in order):
        try:
            result = eval(order)
            print(f'계산 결과는 {result} 입니다.')
            my_money_book['계산기'] = (my_date(), '계산기', '계산기', 0, order)
        except (SyntaxError, NameError):
            print("잘못된 입력입니다. 올바른 계산식을 입력해주세요.")
    else:
        print("잘못된 입력입니다. 올바른 계산식을 입력해주세요.")
