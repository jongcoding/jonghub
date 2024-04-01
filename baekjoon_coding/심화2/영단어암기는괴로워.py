import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words = {}

for _ in range(n):
    a = input().rstrip()
    if m <= len(a):
        if a in words:
            words[a] += 1
        else:
            words[a] = 1
def custom_sort(word):
    frequency = words[word]
    length = len(word)
    return (-frequency, -length, word)
b= sorted(words, key=custom_sort)
print('\n'.join(map(str, b)))