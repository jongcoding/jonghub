import sys
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b
n = int(sys.stdin.readline().rstrip())
count_iterative = n - 2
fibonacci_number = fibonacci(n)
print(fibonacci_number, count_iterative)
