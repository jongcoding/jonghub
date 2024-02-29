n= int(input())
num=0
for i in range(n):
    result=1
    word=list(input())
    con=list(set(word))
    for hi in con:
        cnt= word.count(hi)
        for j in range(cnt):
            p=word.index(hi)
            if word[p+j]==hi:
                pass
            else:
                result=0
    if result==1:
        num+=1
print(num)


# 최적화 코드
n = int(input())
count_group_words = 0

for _ in range(n):
    word = input()
    visited = set()  # 각 문자의 등장 여부를 저장할 집합

    is_group_word = True
    prev_char = ''  # 이전 문자를 저장하는 변수

    for char in word:
        if char != prev_char:  # 현재 문자가 이전 문자와 다를 때
            if char in visited:  # 현재 문자가 이미 등장한 적이 있는 경우
                is_group_word = False
                break
            visited.add(char)  # 현재 문자를 집합에 추가
            prev_char = char  # 이전 문자를 현재 문자로 업데이트
        else:
            continue

    if is_group_word:
        count_group_words += 1

print(count_group_words)

           



        
        




