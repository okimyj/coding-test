
import math
def stringDateToDayNum(date) :
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    # today datetime 객체로 변환
    todayY, todayM, todayD = map(int, today.split('.'))
    todayNum = stringDateToDayNum(today)
    termsDic = {}
    for item in terms :
        kind, month = item.split(' ')
        termsDic[kind] = int(month)
    
    answer = []    
    for i, privacie in enumerate(privacies) :
        expireDate, kind = privacie.split(' ')
        expireDateNum = stringDateToDayNum(expireDate)
        expireDateNum += termsDic[kind] * 28
        print("today : ", today, " expireDate : ", expireDate, " todayNum : ", todayNum, " expireDateNum : " , expireDateNum)
        if expireDateNum <= todayNum :
            answer.append(i+1)
        # print("origin expire : ", expireDate)
        # year, month, day = map(int, expireDate.split('.'))
        # month+=termsDic[kind]
#         day-=1
#         if day == 0:
#             day = 28
#             month-=1
#         if month == 0 :
#             year -=1
#             month = 12
#         year += math.floor(month/13)
        
        
#         month = month%13
#         if month == 0:
#             month=1
        
        # expireDate = datetime(year, month, day)
        
        # # print("today : " , today, "expireDate : " , expireDate)
        # # if expireDate < today :
        # #     answer.append(i+1)
        
        
    
    
    return answer