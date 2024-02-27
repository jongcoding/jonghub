while True:
    try:
        a = input()
        print(a)
    except EOFError:  # 입력의 끝 (End of File) 예외 처리
        break