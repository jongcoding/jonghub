# 반복가능한 데이터 x를 입력 값으로 받으며 이 x의 요소가 모두 참이면  True, 거짓이 하나라도 있으면 False를 리턴한다.
print(all([1, 2, 3])) # TRUE
print(all([1, 2, 3,0])) #FALSE
print(all([])) # TRUE