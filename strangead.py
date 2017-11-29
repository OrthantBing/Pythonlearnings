"""
initial = 5

#day 1

day1 = 5 // 2

#day 2
day2 = (day1 * 3) // 2

#day 3
day3 = (day2 * 3) // 2
"""
def counttoday(day,initial=5):
    count, yesterday = 0,0
    for i in range(1,day+1):
        if i == 1:
            yesterday = initial // 2
            count += yesterday
        else:
            yesterday = (yesterday * 3) // 2
            count += yesterday
    return count

print counttoday(3)
print counttoday(4)
