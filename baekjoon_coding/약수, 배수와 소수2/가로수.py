import math
n=int(input())
tree_list=list(int(input()) for _ in range(n))
tree_dis=[]
for i in range(n-1):
    dis=tree_list[i+1]-tree_list[i]
    tree_dis.append(dis)
gcd_gaps= tree_dis[0]
#gcd 함수로 최대공약수를 구함
for gap in tree_dis[1:]:
    gcd_gaps=math.gcd(gcd_gaps, gap)

put_tree=0
#간격을 최대공약수로 나눠서 갯수를 구함 
for gap in tree_dis:
    put_tree+=gap//gcd_gaps-1
print(put_tree)
