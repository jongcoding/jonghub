def modular_exponentiation(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A % C
    
    half = modular_exponentiation(A, B // 2, C)
    
    if B % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * A) % C


A, B, C = map(int, input().split())
print(modular_exponentiation(A, B, C))

#A, B, C = map(int, input().split())

# pow 함수를 사용하여 모듈러 거듭제곱 계산
#result = pow(A, B, C)

# 결과 출력
#print(result)