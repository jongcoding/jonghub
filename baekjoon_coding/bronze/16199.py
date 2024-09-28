from datetime import datetime

birth_year, birth_month, birth_day = map(int, input().split())
reference_year, reference_month, reference_day = map(int, input().split())

birth_date = datetime(birth_year, birth_month, birth_day)
reference_date = datetime(reference_year, reference_month, reference_day)

full_age = reference_year - birth_year - ((reference_month, reference_day) < (birth_month, birth_day))

counting_age = reference_year - birth_year + 1

year_age = reference_year - birth_year

# 결과 출력
print(full_age)
print(counting_age)
print(year_age)
