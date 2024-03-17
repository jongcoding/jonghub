#단어를 뒤에서부터 읽어도 똑같으면 팰린드롬
# 수의 숫자도 뒤에서부터 읽어도 똑같으면 팰린드롬
# 10은 팰린드롬이 아님 앞에 무의미한 0이 오지 않음
def is_palindrom(num):
    for i in range(len(num)//2):
        if num[i]!=num[-i-1]:
            return False
    return True
while True:
    num=int(input())
    if num==0:
        break
    list_num=list(str(num))
    if is_palindrom(list_num):
        print("yes")
    else:
        print("no")
   