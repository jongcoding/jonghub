def compute_score(**scores):
    if not scores:
        print("성적 정보가 없습니다.")
        return
    
    total = sum(scores.values())
    avg = total / len(scores)
    max_student = max(scores, key=scores.get)
    min_student = min(scores, key=scores.get)

    print("\n[성적 산출 결과]")
    for name, score in scores.items():
        print(f"- {name}: {score}점")
    print(f"총점: {total}점")
    print(f"평균: {avg:.1f}점")
    print(f"최고점자: {max_student} ({scores[max_student]}점)")
    print(f"최하점자: {min_student} ({scores[min_student]}점)")

scores = {}
while True:
    choice = input("메뉴: 1=입력 2=성적산출 q=종료 >> ")
    if choice == '1':
        while True:
            entry = input("성적을 입력하세요 (이름=점수): ")
            if entry == '.':
                print("성적이 입력되었습니다.")
                break
            try:
                name, score = entry.split('=')
                scores[name.strip()] = int(score.strip())
            except ValueError:
                print("잘못된 형식입니다. '이름=점수' 형식으로 입력하세요.")
    elif choice == '2':
        compute_score(**scores)
    elif choice.lower() == 'q':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 명령입니다. 다시 입력하세요.")
    print()
