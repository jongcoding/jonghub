# 출력할 함대 정보 리스트
fleet_info = [
    ("N2 Bomber", "Heavy Fighter", "Limited", 21),
    ("J-Type 327", "Light Combat", "Unlimited", 1),
    ("NX Cruiser", "Medium Fighter", "Limited", 18),
    ("N1 Starfighter", "Medium Fighter", "Unlimited", 25),
    ("Royal Cruiser", "Light Combat", "Limited", 4),
]

# 각 열의 너비
column_widths = [15, 15, 11, 10]

# 헤더 출력
print(f"{'SHIP NAME':<{column_widths[0]}}{'CLASS':<{column_widths[1]}}{'DEPLOYMENT':<{column_widths[2]}}{'IN SERVICE':<{column_widths[3]}}")

# 데이터 출력
for ship in fleet_info:
    print(f"{ship[0]:<{column_widths[0]}}{ship[1]:<{column_widths[1]}}{ship[2]:<{column_widths[2]}}{ship[3]:<{column_widths[3]}}")
