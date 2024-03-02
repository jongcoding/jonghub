a,b,v= map(int, input().split())
day_move=a-b
print((v-a+day_move-1)//day_move+1)