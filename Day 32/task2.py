#Task 2 is about datetime

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

print(year)
print(month)
print(day)
print(day_of_week)

date_of_birth = dt.datetime(year=1975,month=10,day=1, hour=4)
print(date_of_birth)