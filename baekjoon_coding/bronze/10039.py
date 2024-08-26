sum=0
for _ in range(5):
    cmd= int(input())
    if cmd <40:
        sum+=40
    else:
        sum+=cmd
print(sum//5)