import sys
# 초기화
Student= list(range(1, 31))
for _ in range(28):
    Student.pop(Student.index(int(input())))
print('\n'.join(map(str,Student)))

# 최적화 코드
#import sys

# 입력 받기
#excluded_students = [int(sys.stdin.readline()) for _ in range(28)]

# 학생 리스트 생성 및 제외(리스트 컴프리 헨션)
#students = [str(student) for student in range(1, 31) if student not in excluded_students]

# 결과 출력
#print('\n'.join(students))