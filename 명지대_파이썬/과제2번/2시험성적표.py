
scores = [55, 35, 40, 70, 65, 30]
below_40 = 0
total = 0

for score in scores:
    if score < 40:
        below_40 += 1
    total += score

num_subjects = len(scores)


average_score = total / num_subjects


if below_40 > 0 or average_score < 60:
    print("40점 미만 과목수 :", below_40)
    print("평균 점수 :", average_score)
    print("아쉽습니다. 불합격하셨습니다.")
else:
    print("축하합니다! 합격하셨습니다.")
