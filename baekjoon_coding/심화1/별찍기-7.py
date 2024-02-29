n=int(input())
a=2*n-1

for i in range(a):
    for j in range(a):

        if abs(i-n+1)<j+1<2*n-abs(i-n+1):
            print("*", end="")
        else:
            if j+1<2*n-abs(i-n+1):
                print(" ", end="")
        
    print("")

# 최적화 코드
def print_diamond(n):
    for i in range(-n+1, n):
        line = ""
        for j in range(-n+1, n):
            if abs(i) + abs(j) < n:
                line += "*"
            else:
                line += " "
        print(line)

n = int(input("Enter a number: "))
print_diamond(n)