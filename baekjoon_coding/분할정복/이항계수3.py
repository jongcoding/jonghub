p=1000000007

# 페르마의 소정리 a^(p-1)=1 (mod p)
# a^(p-2)=a^-1 (mod p)

def factorial(x):
    res=1
    for i in range(2,x+1):
        res=(res*i)%p
    return res
def comb(n,k):
    n_f=factorial(n)
    modd=factorial(k)*factorial(n-k)%p
    inv=mod(modd,p-2)
    result=n_f*inv%p
    print(result)
def mod(a,b):
    return pow(a,b,p)

def main():
    n,k=map(int, input().split())
    comb(n,k)
if __name__=='__main__':
    main()