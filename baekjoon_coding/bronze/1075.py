n=list(input())
f=int(input())

for i in range(10):
    for j in range(10):
        n[-2]=str(i)
        n[-1]=str(j)
        if int("".join(map(str, n)))%f==0:
            print(f"{i}{j}")
            exit()
