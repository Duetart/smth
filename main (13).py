import datetime
date = input("YYYY.MM.DD:")
year, month, day = map(int, date.split("."))
date1 = datetime.date(year, month, day)
today=datetime.date.today()
print(today.year - date1.year - ((today.month, today.day) < (date1.month, date1.day)))