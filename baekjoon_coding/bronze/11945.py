
N, M = map(int, input().split())
bread = [input().strip() for _ in range(N)]
flipped_bread = [row[::-1] for row in bread]
for row in flipped_bread:
    print(row)
