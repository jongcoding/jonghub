def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    print(total_fee(n))

def total_fee(n):
    p = 4000
    total_cost = n * p
    return total_cost

if __name__ == "__main__":
    main()
