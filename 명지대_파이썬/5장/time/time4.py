import datetime

d= datetime.datetime.now()
print(d)
print(d.year, d.month, d.day, sep='/')
print(d.hour, d.minute, d.second, d.microsecond, sep=':')
print(d.weekday())