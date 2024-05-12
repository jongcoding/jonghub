#1km다 1리터 기름사용
#최소의 비용을 계산하는 프로그램
# 일단 현재 도시의 가격보다 싼곳까지 탐색
# 그다음 거기까지의 기름값을 계산
# 그다음 싼곳에서 그다음 싼곳까지 거리 탐색
# 기름값게싼
n= int(input())
lenght=list(map(int, input().split()))
price=list(map(int, input().split()))
sum_price=0
min_price=price[0]
for i in range(n-1):
    if price[i]>min_price:
        sum_price+=min_price*lenght[i]
    elif price[i]<=min_price:
        min_price=price[i]
        sum_price+=min_price*lenght[i]
print(sum_price)
