def check(n, screen, color):
    for y in range(n):
        for x in range(n):
            if screen[y][x] != color:
                return False
    return True

def Quad_Tree(n, screen):
    color = screen[0][0]
    if n == 1:
        return str(color)
    if check(n, screen, color):
        return str(color)
    
    result = "("
    new_screen = [[], [], [], []]
    for i in range(n // 2):
        new_screen[0].append(screen[i][:n // 2])
        new_screen[1].append(screen[i][n // 2:])
        new_screen[2].append(screen[n // 2 + i][:n // 2])
        new_screen[3].append(screen[n // 2 + i][n // 2:])
    
    for i in range(4):
        result += Quad_Tree(n // 2, new_screen[i])
    result += ")"
    
    return result

# 입력 받기
n = int(input("한 줄에 들어갈 숫자의 개수를 입력하세요: "))
screen = [[int(num) for num in input().strip()] for _ in range(n)]

# Quad_Tree 함수 호출 및 결과 출력
result = Quad_Tree(n, screen)
print(result)
