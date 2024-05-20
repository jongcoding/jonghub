def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

def f_to_c(f):
    return (f - 32.0) * 5.0 / 9.0

def main():
    while True:
        choice = input("메뉴: 1=섭씨->화씨, 2=화씨->섭씨, q=종료 >> ")
        if choice == '1':
            c = float(input("섭씨 온도를 입력하세요: "))
            f = c_to_f(c)
            print(f"{c:.2f}도는 화씨로 {f:.2f}도입니다.")
        elif choice == '2':
            f = float(input("화씨 온도를 입력하세요: "))
            c = f_to_c(f)
            print(f"{f:.2f}도는 섭씨로 {c:.2f}도입니다.")
        elif choice.lower() == 'q':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력하세요.")
        print()
if __name__ == "__main__":
    main()
