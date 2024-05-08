# 초기 프린터 목록과 각 프린터의 종이 및 토너 수량
printers = {
    '잉크젯': [200, 100],
    '레이저젯': [200, 100],
    'Epson': [200, 100]
}

# 초기 예산
budget = 200000

# 프로그램 시작 메시지
print("프린터 관리자입니다")
print("=" * 50)

# 프로그램 루프
while True:
    command = input("명령을 입력하세요 (1=사용 2=상태 3=보충 4=종료) >> ")

    if command == '1':
        # 사용 명령
        try:
            entry = input("프린터와 장수를 입력하세요 (예: 잉크젯 20) >> ")
            printer_name, pages_str = entry.split()
            pages = int(pages_str)

            if printer_name in printers:
                paper, toner = printers[printer_name]

                if pages <= paper:
                    paper -= pages
                    toner_used = pages // 10
                    toner = max(0, toner - toner_used)
                    printers[printer_name] = [paper, toner]
                else:
                    print("종이가 부족합니다.")
            else:
                print("해당 프린터가 존재하지 않습니다.")

        except ValueError:
            print("올바른 형식으로 입력해 주세요 (예: 잉크젯 20).")

    elif command == '2':
        # 상태 명령
        for name, (paper, toner) in printers.items():
            print(f"{name} 종이 {paper} 토너 {toner}")
        print(f"잔액은 {budget}원")

    elif command == '3':
        # 보충 명령
        try:
            entry = input("프린터와 장수 및 토너수를 입력하세요 (예: 잉크젯 100 50) >> ")
            printer_name, paper_str, toner_str = entry.split()
            paper_add = int(paper_str)
            toner_add = int(toner_str)

            # 비용 계산
            paper_cost = paper_add * 100
            toner_cost = toner_add * 200
            total_cost = paper_cost + toner_cost

            if total_cost <= budget:
                budget -= total_cost

                if printer_name in printers:
                    paper, toner = printers[printer_name]
                    printers[printer_name] = [paper + paper_add, toner + toner_add]
                else:
                    printers[printer_name] = [paper_add, toner_add]
            else:
                print("예산이 부족합니다.")

        except ValueError:
            print("올바른 형식으로 입력해 주세요 (예: 잉크젯 100 50).")

    elif command == '4':
        # 종료 명령
        print("프로그램을 종료합니다")
        break

    else:
        print("잘못된 명령입니다. 다시 시도하세요.")
    print()
