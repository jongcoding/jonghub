# 가계부 초기 설정
my_book = {'점심': 10000, '커피': 3000}

# 프로그램 실행 루프
while True:
    # 사용자에게 명령 입력 요청
    command = input('명령을 입력하세요 (1=입력 2=상태 3=삭제 4=종료) >> ')

    if command == '1':
        # 새 항목과 가격을 입력받아 가계부에 추가
        try:
            entry = input('항목과 가격을 입력하세요 (예: 점심 10000) >> ')
            item, price = entry.split()
            my_book[item] = int(price)
        except ValueError:
            print("올바른 형식으로 입력해 주세요 (예: 점심 10000).")

    elif command == '2':
        # 가계부 항목과 총액 출력
        total = 0
        for item, price in my_book.items():
            print(f'항목 {item} 금액 {price}')
            total += price
        print(f'총액 {total} 원')

    elif command == '3':
        # 삭제할 항목을 입력받아 가계부에서 제거
        item_to_remove = input('삭제 항목을 입력하세요 (예: 점심) >> ')
        if item_to_remove in my_book:
            del my_book[item_to_remove]
            print(f'{item_to_remove} 항목이 삭제되었습니다.')
        else:
            print('해당 항목이 존재하지 않습니다.')

    elif command == '4':
        # 프로그램 종료
        print('프로그램을 종료합니다.')
        break

    else:
        print('잘못된 명령입니다. 다시 시도하세요.')
    print()