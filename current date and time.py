from datetime import date, time, datetime

today = date.today()
print(today)

now = datetime.now
print(now)

print(f"current year: {today.year}")
print(f"current month: {today.month}")
print(f"current day: {today.day}")