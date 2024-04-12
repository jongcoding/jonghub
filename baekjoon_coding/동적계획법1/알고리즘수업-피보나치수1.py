import sys
n = int(sys.stdin.readline().rstrip())
a, b = 1, 1
for _ in range(n - 2):
    a, b = b, a + b
print(b, n-2)
