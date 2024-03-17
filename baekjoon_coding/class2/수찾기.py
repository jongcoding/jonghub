# n개의 정수 A[1]~A[N] 이 주어졌을 때 X라는 정수가 존재하는 알아내는 프로그램
# 시간을 빨리 검색하려면 set을 사용해야 함
N=int(input())
num_list=set(map(int, input().split()))
m=int(input())
search_list=list(map(int, input().split()))
for num in search_list:
    if num in num_list:
        print(1)
    else:
        print(0)