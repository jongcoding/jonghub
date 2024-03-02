a=int(input())
for i in range(a):
    N=float(input())
    q=25.0
    d=10.0
    n=5.0
    p=1.0
    print(int(N//q),int((N%q)//d),int(((N%q)%d)//n),int((((N%q)%d)%n)//p))

    # 최적화 코드
    a = int(input())
    for _ in range(a):
        N = int(input())
        q = 25
        d = 10
        n = 5
        p = 1
        quarters = N // q
        dimes = (N % q) // d
        nickels = ((N % q) % d) // n
        pennies = (((N % q) % d) % n) // p
        print(quarters, dimes, nickels, pennies)
