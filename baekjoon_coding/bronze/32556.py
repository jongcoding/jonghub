from collections import defaultdict

def count_substrings(s):
    # 문자의 등장 횟수를 저장하는 딕셔너리
    char_count = defaultdict(int)
    
    n = len(s)
    
    # 각 문자에 대해서 해당 문자가 포함된 부분 문자열 수를 카운트
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            for char in set(substring):  # 중복된 문자 카운팅 방지
                char_count[char] += 1
    
    return char_count

def run_length_encoding(s):
    # 문자열의 run length encoding을 통해 각 문자와 그 횟수를 출력
    result = defaultdict(int)
    prev_char = None
    count = 0
    for char in s:
        if char == prev_char:
            count += 1
        else:
            if prev_char is not None:
                result[prev_char] += count
            prev_char = char
            count = 1
    if prev_char is not None:
        result[prev_char] += count
    
    return result

def solve(s):
    # 각 문자별 등장 횟수를 집계
    char_count = run_length_encoding(s)
    
    # 결과 출력 (ASCII 순으로 정렬)
    for char in sorted(char_count.keys()):
        print(f"{char} {char_count[char]}")

# 예제 입력
input_str = "ABC"
solve(input_str)

input_str = "aaaab"
solve(input_str)
