# 첫줄에 테스츠 케이스의 수

# 테스트 케이스 첫번쨰 줄 
# 문서 갯수n
# 문서가 현재 queue에서 몇 번쨰 놓였는지 m
# 맨 왼쪽 0번쨰
# queue의 가장 앞에있는 문서의 중요도 파악
# 나머지 문서들 중 현재 문서보다 중요독 높은 문서가 하나라도 있으면 
# 이 문서를 인쇄하지 않고 queue의 가장 뒤에 재배치
# 그렇지 않다면 바로 인쇄
from collections import deque
test_case=int(input())
for _ in range(test_case):
    n,m=map(int, input().split())
    importance=deque(list(map(int, input().split())))
    count=0
    que=[m]
    while True:
        max_importance=max(importance)
        if importance[0]==max_importance and que[0]==0:
            count+=1
            print(count)
            break
        elif importance[0]==max_importance and que[0]!=0:
            count+=1
            importance.popleft()
            que[0]-=1
        elif importance[0]!=max_importance:
            if que[0]==0:
                q=importance.popleft()
                importance.append(q)
                que[0]=len(importance)-1
            elif que[0]!=0:
                q=importance.popleft()
                importance.append(q)
                que[0]-=1

            
