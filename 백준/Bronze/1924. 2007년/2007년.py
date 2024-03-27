import sys
month, day = list(map(int, sys.stdin.readline().split(' ')))
weekDays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
monthDays = {}
def addMonthDays(monthArr, days) :
    for m in monthArr :
        monthDays.update({m : days})

addMonthDays([1, 3, 5, 7, 8, 10, 12], 31)
addMonthDays([4, 6, 9, 11], 30)
addMonthDays([2], 28)

totalDays = day -1
for i in range(1, month) :
    totalDays += monthDays.get(i)

print(weekDays[totalDays%len(weekDays)])

