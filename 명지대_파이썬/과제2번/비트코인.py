print("가상화폐 프로그램에 오신 것을 환영합니다")
print("===================================")
print("가상화폐 프로그램에 오신 것을 환영합니다")
# 초기 코인 데이터
coins = [['BTC', 50000], ['XRP', 20000], ['ADA', 30000]]

while True:
    command = input("명령을 입력하세요 (1=입력, 2=내역확인, 3=삭제, q=종료) >> ")
    if command == 'q':
        print("프로그램을 종료합니다.")
        break

    if command == '1':
        while True:
            coin_info = input("코인 정보를 입력하세요 (입력종료는 마침표) >> ")
            if coin_info == '.':
                break
            parts = coin_info.split()
            if len(parts) == 2 and parts[1].isdigit():
                name, amount = parts
                amount = int(amount)
                found = False
                for coin in coins:
                    if coin[0] == name:
                        coin[1] += amount
                        found = True
                        break
                if not found:
                    coins.append([name, amount])
            else:
                print("잘못된 입력입니다. 형식: 코인명 금액")

    elif command == '2':
        if coins:
            print("현재 보유중인 가상화폐 내역입니다")
            total_amount = sum(coin[1] for coin in coins)
            coin_details = ', '.join(f"{coin[0]} {coin[1]} 원" for coin in coins)
            print(coin_details)
            print(f"총 보유액은 {total_amount} 원입니다")
        else:
            print("보유중인 코인이 없습니다.")

    elif command == '3':
        if coins:
            coin_name = input("삭제할 코인을 입력하세요 >> ")
            initial_length = len(coins)
            coins = [coin for coin in coins if coin[0] != coin_name]
            if len(coins) == initial_length:
                print("해당 코인이 없습니다.")
        else:
            print("삭제할 코인이 없습니다.")
    else:
        print("잘못된 명령입니다. 명령은 1, 2, 3, q 중 하나입니다.")

    print()
