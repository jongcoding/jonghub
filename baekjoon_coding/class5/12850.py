MOD = 1000000007

# 인접 행렬
v = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

# 행렬 곱셈 함수
def multiply(M1, M2):
    size = len(M1)
    ret = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            elem = 0
            for k in range(size):
                elem += (M1[i][k] * M2[k][j]) % MOD
            ret[i][j] = elem % MOD
    return ret

# 행렬 거듭제곱 함수
def matrix_pow(mat, exp):
    size = len(mat)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    factor = mat
    
    while exp > 0:
        if exp % 2 == 1:
            result = multiply(result, factor)
            exp -= 1
        factor = multiply(factor, factor)
        exp //= 2
    
    return result

# 메인 함수
def main(D):
    # D제곱한 결과에서 정보과학관(0번)에서 다시 정보과학관(0번)으로 돌아오는 경우의 수
    result = matrix_pow(v, D)
    return result[0][0]

# 예제 실행
D = int(input())
print(main(D))  # 출력: 정답은 모듈러 연산된 값
