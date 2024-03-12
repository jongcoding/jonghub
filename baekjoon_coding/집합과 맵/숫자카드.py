# 속도를 최적화하기 위해서는 num_list1을 
#집합(set)으로 변환하여 탐색을 더 빠르게 할 수 있음. 
#집합은 해시 테이블을 사용하기 때문에 탐색에 
#상수 시간(평균적으로 O(1))이 걸리므로 더 빠름

n1=int(input())
num_list1=set(map(int, input().split()))
n2=int(input())
num_list2=list(map(int, input().split()))
result_list=[]
for num in num_list2:
    if num in num_list1:
        result_list.append(1)
    else:
        result_list.append(0)
print(*result_list)