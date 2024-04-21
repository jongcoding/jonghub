# 규칙 두가지
# 포도주 잔을 선택-> 그 잔에 들어있는 포도주 다마셔야함
# 마신 후-> 원래위 치에 잔을 다시 놓아야함
# 연속으로 놓여있는 3잔을 모두 마실 수 없음
# 최대로 많은 포도주를 마실수 있는 알고리즘짜기
import sys
input=sys.stdin.readline
def drink_wine_max(wine_list,n):
    dp=[0]*n
    dp[0]=wine_list[0]
    if n==1:
          return dp[0]
    elif n==2:
          return wine_list[0]+wine_list[1]
    dp[1]=wine_list[0]+wine_list[1]
    dp[2]=max(dp[0]+wine_list[2],dp[1],wine_list[1]+wine_list[2])
    for i in range(3,n):
         dp[i]=max(dp[i-1],dp[i-2]+wine_list[i],dp[i-3]+wine_list[i-1]+wine_list[i])
    return dp[-1]
n= int(input().rstrip())
# 포도주양은 1000이하의 음아 아닌 정수
wine_list=[int(input().rstrip()) for _ in range(n)]
print(drink_wine_max(wine_list,n))
