data=[]
x=y=best=0
for i in range(9):
    data.append(list(map(int,input().split())))
    for j in range(9):
        if data[i][j]>best:
            best=data[i][j]
            x=i
            y=j
print(best)
print(x+1,y+1)

#최적화 코드
best = 0
best_x = best_y = 0

for i in range(9):
    row = list(map(int, input().split()))
    max_in_row = max(row)
    if max_in_row > best:
        best = max_in_row
        best_x = i
        best_y = row.index(best) 

print(best)
print(best_x + 1, best_y + 1)