# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼
# 사람들을 데려와 살아야 한다.
# 주어지는 양의 정수k와
# n에 대해 k층에 n호에는 
# 몇 명이 살고 있는 지 출력
# 0층부터 있고 각층에있는 1호부터있음
# 0층의 i호는 i명이 산다.
t=int(input())
for _ in range(t):
    k=int(input())
    n=int(input())
    array=list(range(1,n+1)) #0층
    result_array=[0]*n   
    for i in range(1,k+1):
        result_array=[0]*n
        for j in range(n):
            for p in range(j+1):
                result_array[j]+=array[p]
        for p in range(j+1):
            array[p]=result_array[p]
    print(result_array[n-1])
