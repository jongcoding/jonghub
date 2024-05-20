def hapcha(a,b,op):
    if op=="+":
        result=hap(a,b)
        print(f"{a} {b} 의 합은  {result} 입니다")
    elif op=="-":
        result=cha(a,b)
        print(f"{a} {b} 의 차는  {result} 입니다")
    else:
        print("정의되지 않은 연산입니다")
def hap(a,b):
    print("두 수의 합을 구해 출력해주는 함수입니다")
    return a+b
def cha(a,b):
    print("두 수의 차를 구해 출력해주는 함수입니다")
    return a-b

hapcha(10, 20, '+')
hapcha(10, 20, '-')
hapcha(-87, 172, '+')
hapcha(-87, 172, '-')
hapcha(-87, 172, '*')