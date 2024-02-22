H, M= map(int, input().split())
if M >= 45:
    print(H,M-45)
else:
    if H >0:
        print(H-1,15+M)
    else:
        print(23,15+M)

# SHORT CODING
# H,M=map(int,input().split())
# print((H-(M<45))%24,(M-45)%60)