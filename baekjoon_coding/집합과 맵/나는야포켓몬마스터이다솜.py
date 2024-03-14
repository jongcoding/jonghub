# 포켓몬 도감을 입력 받고 딕셔너리로 저장하는 함수
def make_pokedex(N):
    pokedex = {}
    for i in range(N):
        pokemon_name = input().strip()
        pokedex[pokemon_name] = i + 1
    return pokedex

# 문제를 입력 받고 각각에 대한 답을 출력하는 함수
def solve(pokedex, pokedex_reverse, M, questions):
    answers = []
    for question in questions:
        if question.isdigit():  # 입력이 숫자인 경우
            question = int(question)
            answers.append(pokedex_reverse[question])
        else:  # 입력이 문자인 경우
            answers.append(str(pokedex[question]))
    return answers

# 메인 함수
def main():
    N, M = map(int, input().split())
    pokedex = make_pokedex(N)
    pokedex_reverse = {v: k for k, v in pokedex.items()} # 번호를 key로, 이름을 value로 바꾼 딕셔너리
    questions = [input().strip() for _ in range(M)] # 입력 받기를 한 번에 처리하여 리스트로 저장
    answers = solve(pokedex, pokedex_reverse, M, questions)
    for answer in answers:
        print(answer)

# 실행
if __name__ == "__main__":
    main()