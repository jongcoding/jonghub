a= int(input())
t=[]
for _ in range(a):
    b,c=map(str, input().split())
    for i in range(len(c)):
        t.append(c[i]*int(b))
    print(''.join(map(str,t)))
    t=[]

# 최적화코드
#a = int(input())

#for _ in range(a):
#    b, c = input().split()
#    result = ''.join(c * int(b) for _ in range(len(c)))
#    print(result)