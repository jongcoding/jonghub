# 첫번째 인수로 함수, 두번 째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다.
# 그리고 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 리턴값이 참인 것만 묶어서 리턴한다.
def positive(x):
    return x>0
print(list(filter(positive, [1,-3,2,0,-5,6])))
