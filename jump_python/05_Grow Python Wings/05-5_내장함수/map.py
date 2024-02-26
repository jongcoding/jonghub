# 함수와 반복 가능한 데이터를 입력으로 받는다.
# map은 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴
def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result
result=two_times([1,2,3,4])
print(result)