def get_hangul_character(n):
    # 초성, 중성, 종성의 개수
    initial_consonants = 19
    medial_vowels = 21
    final_consonants = 28
    
    # 유니코드 한글 시작점
    unicode_start = 0xAC00
    
    # 초성, 중성, 종성 인덱스 계산
    initial_index = (n - 1) // (medial_vowels * final_consonants)
    medial_index = ((n - 1) % (medial_vowels * final_consonants)) // final_consonants
    final_index = (n - 1) % final_consonants
    
    # 유니코드 값 계산
    unicode_value = unicode_start + (initial_index * medial_vowels * final_consonants) + (medial_index * final_consonants) + final_index
    
    # 유니코드를 문자로 변환하여 반환
    return chr(unicode_value)

# 예제 입력
n = int(input())
print(get_hangul_character(n))
