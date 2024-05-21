import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
omega_1 = []
for i in range(n):
    omega_1.append(list(map(int, input().rstrip().split())))

m, k = map(int, input().rstrip().split())
omega_2 = []
for i in range(m):
    omega_2.append(list(map(int, input().rstrip().split())))
result = [[0 for _ in range(k)] for _ in range(n)]


for i in range(n):
    for j in range(k):
        for l in range(m):
             result[i][j]+=omega_1[i][l]*omega_2[l][j]

for num in result:
        print(' '.join(map(str, num)) )
