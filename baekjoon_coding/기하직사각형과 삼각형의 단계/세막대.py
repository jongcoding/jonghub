a,b,c=map(int, input().split())
list_num=[a,b,c]
list_num.sort()
if list_num[2]-list_num[0]-list_num[1]>0:
    print(a+b+c-(list_num[2]-list_num[0]-list_num[1])-1)
elif list_num[2]-list_num[0]-list_num[1]==0:
    print(a+b+c-1)
else:
    print(a+b+c)