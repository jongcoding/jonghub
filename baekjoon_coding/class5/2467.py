import sys
input=sys.stdin.readline
def find_closest_to_zero(arr,n):
    left, right = 0, n- 1
    closest_sum = float('inf')
    result = (0, 0)

    while left < right:
        current_sum = arr[left] + arr[right]

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = (arr[left], arr[right])

        if current_sum < 0:
            left += 1
        else:
            right -= 1
    return result
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
solution = find_closest_to_zero(arr,n)
print(solution[0], solution[1])
