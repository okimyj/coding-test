def solution(a, b):
    def getDayNum(month):
        if month == 2:
            return 29       # 윤년이니까 29
        if month < 8 :
            return month %2 == 0 and 30 or 31
        return month %2 == 0 and 31 or 30
    # 각 월의 날짜 수 객체 생성.
    days = {m:getDayNum(m) for m in range(1,13)}
    dayOfWeek = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    
    # a월 b일까지 전체 날짜 수 합산
    totalDays = b
    for month in range(1, a) :
        totalDays += days[month]
    
    # 요일 인덱스 (1월 1일이 금요일이니까 +4)
    dayOfWeekIndex = (totalDays+4)%7

    print(dayOfWeekIndex)
    answer = dayOfWeek[dayOfWeekIndex]
    return answer