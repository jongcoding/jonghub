
while True:
    num_list=[]
    sum=0
    n= int(input())
    if n==-1:
        break
    for i in range(1, n):
        if n%i==0:
            num_list.append(i)
            sum+=i
    if sum==n:
        print(n,"= ",end="")
        for j in range(len(num_list)):
            if len(num_list)==j+1:
                print(num_list[j])
            else:
                print(num_list[j],"+ ",end="") 
    else:
        print(n,"is NOT perfect.")

# 최적화 코드
# n이 자신보다 작은 수의 배수가 아니라면 자신의 절반이 넘어가는 수는 약수가 될 수 없기 때문
        
while True:
    n = int(input())
    if n == -1:
        break

    sum_of_divisors = 0
    divisors = []

    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisors.append(i)
            sum_of_divisors += i

    if sum_of_divisors == n:
        print(f"{n} = ", end="")
        for j in range(len(divisors)):
            if j == len(divisors) - 1:
                print(divisors[j])
            else:
                print(divisors[j], "+ ", end="")
    else:
        print(f"{n} is NOT perfect.")
