import sys
input=sys.stdin.readline
def recursion(s, l ,r, count):
    count+=1
    if l >= r:
        return 1, count
    else:
        if(s[l] != s[r]): 
            return 0, count
        else:
            return recursion(s, l+1, r-1,count)
def isPalindrome(s):
    count=0
    return recursion(s, 0, len(s)-1, count)
t= int(input())
for _ in range(t):
    s=list(input().rstrip())
    print(*isPalindrome(s))