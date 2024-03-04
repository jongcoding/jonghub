while True:
    a,b,c=map(int, input().split())
    if a==b==c==0:
        break
    list=[a,b,c]
    list.sort()
    if max(list)-list[0]-list[1]>=0:
        print("Invalid")
    else:
        if a==b==c:
            print("Equilateral ")
        elif a==b or b==c or c==a:
            print("Isosceles")
        elif a!=b!=c:
            print("Scalene")
 
    