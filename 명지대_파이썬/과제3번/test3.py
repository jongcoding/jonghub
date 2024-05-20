# 초기 프린터 사전과 예산 설정
printer_dict = {
    '잉크젯': [200, 100],
    '레이저젯': [200, 100],
    'Epson': [200, 100]
}
budget = 200000

def cmd_input():
    return input("명령을 입력하세요 (1=사용 2=상태 3=보충 4=등록 5=삭제 q=종료) >> ")

def printer_use(name, pages):
    if name in printer_dict:
        if printer_dict[name][0] >= pages and printer_dict[name][1] >= pages // 10:
            printer_dict[name][0] -= pages
            printer_dict[name][1] -= pages // 10
        else:
            print("프린터의 종이 또는 토너가 부족합니다.")
    else:
        print(f"{name} 프린터가 존재하지 않습니다.")

def printer_status():
    for name, (paper, toner) in printer_dict.items():
        print(f"{name} 종이 {paper} 토너 {toner}")
    print(f"예산 {budget}원")

def printer_refill(name, pages, toner):
    global budget
    cost = pages * 100 + toner * 200
    if budget >= cost:
        if name in printer_dict:
            printer_dict[name][0] += pages
            printer_dict[name][1] += toner
            budget -= cost
        else:
            print(f"{name} 프린터가 존재하지 않습니다.")
    else:
        print("예산이 부족합니다.")

def printer_add(name, pages, toner):
    if name not in printer_dict:
        printer_dict[name] = [pages, toner]
    else:
        print(f"{name} 프린터가 이미 존재합니다.")

def printer_del(name):
    if name in printer_dict:
        del printer_dict[name]
        print(f"삭제 후 남아 있는 프린터들: {list(printer_dict.keys())}")
    else:
        print(f"{name} 프린터가 존재하지 않습니다.")
        
print("프런티 관리자입니다")
print("==================================================")
while True:
    cmd = cmd_input()
    if cmd == '1':
        try:
            use_input = input("프린터와 장수를 입력하세요 (예: 잉크젯 20) >> ")
            name, pages = use_input.split()
            printer_use(name, int(pages))
        except ValueError:
            print("잘못된 입력 형식입니다. '프린터명 장수' 형식으로 입력하세요.")
    elif cmd == '2':
        printer_status()
    elif cmd == '3':
        try:
            refill_input = input("프린터와 장수 및 토너를 입력하세요 (예: 잉크젯 100 50) >> ")
            name, pages, toner = refill_input.split()
            printer_refill(name, int(pages), int(toner))
        except ValueError:
            print("잘못된 입력 형식입니다. '프린터명 장수 토너' 형식으로 입력하세요.")
    elif cmd == '4':
        try:
            add_input = input("등록할 프린터와 장수 및 토너를 입력하세요 (예: 잉크젯 100 50) >> ")
            name, pages, toner = add_input.split()
            printer_add(name, int(pages), int(toner))
        except ValueError:
            print("잘못된 입력 형식입니다. '프린터명 장수 토너' 형식으로 입력하세요.")
    elif cmd == '5':
        del_input = input("삭제할 프린터를 입력하세요 (예: 잉크젯) >> ")
        printer_del(del_input)
    elif cmd.lower() == 'q':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
    print()