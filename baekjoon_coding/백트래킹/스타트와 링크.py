#n은짝수 모인사람 수
# 스타트팀vs링크팀 
#시너지가 있나봄
#축구를 재밌게 하기위해 능력치 차이를 최소화

def backtracking(n, ability_list, start_team,link_team, result, start,current_sum):
    if len(start_team)==n//2:
        link_team=set(range(1,n+1))-start_team
        link_sum = sum(ability_list[i - 1][j - 1] for i in link_team for j in link_team)
        if current_sum-link_sum==0:
            print(0)
            exit() 
        result.add(abs(current_sum - link_sum))
        return result
    for i in range(start,n+1):
            start_team.add(i)
            a=sum(ability_list[i - 1][j - 1] for j in start_team if j != i)
            b=sum(ability_list[j - 1][i - 1] for j in start_team if j != i)
            start_sum = current_sum + a+b
            backtracking(n, ability_list, start_team,link_team, result, i+1,start_sum)
            start_team.remove(i)    
def team_division(n, ability_list):
    start_team=set()
    link_team=set()
    result=set()
    start=1
    initial_sum = 0
    backtracking(n, ability_list, start_team,link_team, result,start,initial_sum)
    print(min(result))
#첫째줄에 스타트팀과 링크 팀의 능력치차이의 최솟값 출력
n= int(input())
ability_list=[list(map(int, input().split())) for _ in range(n)]
team_division(n, ability_list)

