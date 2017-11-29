from datetime import datetime

date2 = datetime(*[i for i in reversed(map(int,raw_input().split()))])
date1 = datetime(*[i for i in reversed(map(int,raw_input().split()))])

fine = 0
if (date2 - date1).days <= 0:
    pass
elif date1.day != date2.day and date1.month == date2.month and date1.year == date2.year:
    fine = 15 * (date2-date1).days
elif date1.month != date2.month and date1.year == date2.year:
    fine = 500 * (date2.month - date1.month)
elif date1.year != date2.year:
    fine = 10000

print fine
