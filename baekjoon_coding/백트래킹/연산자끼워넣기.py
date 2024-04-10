import sys

def cal(num, i, formula):
    # 연산에 따라 결과를 업데이트하는 함수
    # 더하기
    if i == 0:
        formula += num
    #뺼셈
    elif i == 1:
        formula -= num
    #곱셈
    elif i == 2:
        formula *= num
    #나눗셈
    elif i == 3:
        if formula < 0:
            formula = -(-formula // num)
        else:
            formula = formula // num
    return formula

def backtracking(num_list, result, total, calculate, formula, expression):
    if total == len(num_list) - 1:
        result.append(formula)
        return
    for i in range(4):
        if calculate[i] > 0:
            calculate[i] -= 1
            new_formula = cal(num_list[total + 1], i, formula)
            backtracking(num_list, result, total + 1, calculate, new_formula, expression)
            calculate[i] += 1  # 다음 연산을 위해 사용된 연산자 개수를 복구

input = sys.stdin.readline
n = int(input().rstrip())
num_list = list(map(int, input().rstrip().split()))
calculate = list(map(int, input().rstrip().split()))
result = []
expression = [num_list[0]]  # 초기 식은 첫 번째 숫자부터 시작
backtracking(num_list, result, 0, calculate, num_list[0], expression)
print(max(result))
print(min(result))
