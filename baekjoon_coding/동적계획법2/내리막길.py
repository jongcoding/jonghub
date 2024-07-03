def find(m,n, map_list):
    x=0
    y=0
    dp=[[0 for _ in range(m)] for _ in range(n)]
    print(dp)

m, n= map(int, input().split())
map_list=[list(map(int,input().split())) for _ in range(m)]
find(m,n,map_list)
