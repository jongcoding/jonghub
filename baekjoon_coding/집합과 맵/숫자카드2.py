def count_cards(cards, numbers_to_find):
    card_counts = {}
    for card in cards:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1
    result = []
    for num in numbers_to_find:
        if num in card_counts:
            result.append(card_counts[num])
        else:
            result.append(0)
    
    return result


# 입력 받기
N = int(input())  # 상근이가 가지고 있는 숫자 카드의 개수
cards = list(map(int, input().split()))  # 상근이가 가지고 있는 숫자 카드들
M = int(input())  # 구해야 할 숫자의 개수
numbers_to_find = list(map(int, input().split()))  # 구해야 할 숫자들

# 각 숫자별 개수 카운트
result = count_cards(cards, numbers_to_find)

# 결과 출력
print(' '.join(map(str, result)))