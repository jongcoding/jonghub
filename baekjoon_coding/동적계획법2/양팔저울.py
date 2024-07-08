def check(weight_list, check_weight_list):
    max=40000
    dp=[False]*(max+1)
    dp[0]=True
    for weight in weight_list:
        new_possible = dp[:]
        for i in range(max + 1):
            if dp[i]:
                if i + weight <= max:
                    new_possible[i + weight] = True
                if abs(i - weight) <= max:
                    new_possible[abs(i - weight)] = True
        dp = new_possible
    result = []
    for bead in check_weight_list:
        if bead <= max and dp[bead]:
            result.append('Y')
        else:
            result.append('N')
    
    return result

weight=int(input())

weight_list=list(map(int, input().split()))

check_weight=int(input())

check_weight_list=list(map(int, input().split()))


result=check(weight_list, check_weight_list)
print(" ".join(result))