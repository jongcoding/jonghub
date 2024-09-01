import sys
input=sys.stdin.readline
def find_close(n,solution):
    left=0
    right=n-1
    closest_sum = float('inf')
    result=(0,0)
    while left<right:
        current_sum=solution[left]+solution[right]
        if abs(current_sum)<closest_sum:
            closest_sum=abs(current_sum)
            result=(solution[left], solution[right])
        if current_sum<0:
            left+=1
        else:
            right-=1
    return result[0], result[1]
n=int(input().rstrip())
solution=list(map(int, input().split()))
a,b=find_close(n,solution)
print(a,b)

