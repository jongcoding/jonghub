#한 마디로 계속해서 잘람댐
# n은 2,4,8,16,32,64,128 임
# 파란색은 1 흰색은 0
def confetti(n, paper, white_blue):
    color = paper[0][0]
    if n == 1:
        white_blue[color] += 1
        return
    if check(n, paper, color):
        white_blue[color] += 1
        return
    else:
        new_paper = [[], [], [], []]
        for i in range(n // 2):
            new_paper[0].append(paper[i][:n // 2])
            new_paper[1].append(paper[n // 2 + i][:n // 2])
            new_paper[2].append(paper[i][n // 2:])
            new_paper[3].append(paper[n // 2 + i][n // 2:])
        for i in range(4):
            confetti(n // 2, new_paper[i], white_blue)
    return

def check(n, paper, color):
    for y in range(n):
        for x in range(n):
            if paper[y][x] != color:
                return False
    return True

n = int(input())
white_blue = [0, 0]
paper = [list(map(int, input().split())) for _ in range(n)]
confetti(n, paper, white_blue)
print(white_blue[0])
print(white_blue[1])