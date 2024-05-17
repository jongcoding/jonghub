def confetti(n, paper, white_blue):
    color = paper[0][0]
    if n == 1:
        white_blue[color + 1] += 1
        return
    if check(n, paper, color):
        white_blue[color + 1] += 1
        return
    else:
        size = n // 3
        for i in range(3):
            for j in range(3):
                new_paper = [row[j*size:(j+1)*size] for row in paper[i*size:(i+1)*size]]
                confetti(size, new_paper, white_blue)
    return

def check(n, paper, color):
    for y in range(n):
        for x in range(n):
            if paper[y][x] != color:
                return False
    return True

n = int(input())
white_blue = [0, 0, 0]
paper = [list(map(int, input().split())) for _ in range(n)]
confetti(n, paper, white_blue)
print(white_blue[0])  # -1의 개수
print(white_blue[1])  # 0의 개수
print(white_blue[2])  # 1의 개수
