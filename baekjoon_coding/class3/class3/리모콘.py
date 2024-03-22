#첫쨰줄에 이동하려는 채널이 주어짐
# 둘쨰줄에 고장난 버튼의수 
# 셋쨰줄에 고장난 버튼
def make_combination(posible_buttion,N):
    count=0
    leng=list(str(N))
    numbers=0
    number=[0]*len(leng)
    p=0
    pp=0
    if len(posible_buttion)<1:
        return 0
    else:
        for i in range(len(leng)):
            for num in posible_buttion:
                if int(leng[i])>=num:
                    posible_num=num
                    number[i]=[i,num]
            numbers+=(10**i)*posible_num
            count+=1
    for i in range(len(number)):
        num[-1][1]
    print(numbers, count)
    return numbers, count        


N=int(input())
M=int(input())
broken_button=set(map(int, input().split()))
button=set(range(10))
channel=100
possible_button=list(button-broken_button)
main=make_combination(possible_button,N)
num,count=main
count_plusminus=abs(N-num)
print(count_plusminus)
result=count+count_plusminus
print(result)