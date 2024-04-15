from datetime import datetime, timezone, timedelta

# 서울은 UTC+9
seoul_time = datetime.now(timezone(timedelta(hours=9)))
seoul_date = seoul_time.strftime("%Y-%m-%d")

print(seoul_date)