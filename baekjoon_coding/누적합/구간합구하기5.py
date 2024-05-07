import sys
input=sys.stdin.readline
def cumulative_sum(num_list,n):
    cm_sum=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        sum=0
        for j in range(1, n+1):
            sum+=num_list[i-1][j-1]
            cm_sum[i][j]=cm_sum[i-1][j]+sum
    return cm_sum
def cal(cm_sum,x1,y1,x2,y2):
    return cm_sum[x2][y2]-cm_sum[x2][y1-1]-cm_sum[x1-1][y2]+cm_sum[x1-1][y1-1]
if __name__=="__main__":
    
    n,m=map(int, input().rstrip().split())
    num_list=[]
    for i in range(n):
        num_list.append(list(map(int, input().rstrip().split())))
    cm_sum=cumulative_sum(num_list,n)
    for i in range(m):
        x1,y1,x2,y2=map(int, input().rstrip().split())
        print(cal(cm_sum,x1,y1,x2,y2))
    