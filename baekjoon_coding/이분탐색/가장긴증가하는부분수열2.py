from bisect import bisect_left
def length_of_lis(nums):
    sub = []  
    for num in nums:
        pos = bisect_left(sub, num)  
        if pos == len(sub):
            sub.append(num)  
        else:
            sub[pos] = num  
    return len(sub)

n = int(input())
num = list(map(int, input().split()))

print(length_of_lis(num))
