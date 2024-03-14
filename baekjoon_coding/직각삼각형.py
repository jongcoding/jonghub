while True:
    a,b,c=map(int, input().split())
    num_list=[a,b,c]
    num_list.sort()
    if num_list[0]==num_list[1]==num_list[2]==0:
        break
    else:
        if num_list[0]**2+num_list[1]**2==num_list[2]**2:
            print("right")
            print("wrong")
        