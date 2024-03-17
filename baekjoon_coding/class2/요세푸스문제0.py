# 1~n번까지 
# 양의 정수 k가 주어짐
# 순서대로 k번째 사람을 죽임
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정 반복
 
n,k=map(int, input().split())
circle=list(range(1, n+1))
result_list=[]
idx=0
while circle:
    idx=(idx+k-1)%len(circle) # k번째 숫자의 위치
    result_list.append(circle.pop(idx)) # 그 숫자를 제거하면서 결과에 넣기
print('<'+', '.join(map(str, result_list))+'>')