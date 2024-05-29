def mySum(*args):
    return sum(args)
def myAve(*args):
    total = mySum(*args)
    return total / len(args) if args else 0

if __name__ == "__main__":
    print("myCalc 모듈을 직접 실행함")
    print(f'합: {mySum(1, 2, 3, 4)}')
    print(f'평균: {myAve(3, 4, 5, 6, 7):.2f}')
