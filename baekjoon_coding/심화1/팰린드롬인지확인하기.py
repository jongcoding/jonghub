a=list(input())
result=1
len=len(a)
for i in range(len//2):
    if a[i]!=a[len-i-1]:
        result=0
print(result)

# 최적화 코드
#def is_palindrome(input_str):
#    length = len(input_str)
#    for i in range(length // 2):
#        if input_str[i] != input_str[length - i - 1]:
#            return 0
#    return 1

#input_str = input("Enter a string: ")
#print(is_palindrome(input_str))