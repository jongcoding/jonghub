n = int(input())
word_set = set()

# 중복을 제거하면서 단어를 입력 받음
for _ in range(n):
    word = input()
    word_set.add(word)

# 정렬된 단어를 생성
sorted_words = sorted(word_set, key=lambda x: (len(x), x.lower()))

# 정렬된 단어 출력
print("\n".join(sorted_words))
