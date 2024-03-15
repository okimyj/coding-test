def solution(X, Y):
    listX = list(X)
    listY = list(Y)
    intersectList = set(listX) & set(listY)
    # 교집합 개수가 0개면 return -1.
    if len(intersectList) == 0 :
        return "-1"
    
    # 교집합 요소의 합이 0이면 return -1. 
    if sum(map(int, intersectList)) == 0 :
        return "0"
    
    # 교집합 요소를 기준으로 각 숫자마다 가장 적은 개수를 dic에 입력.
    numberCountDic = {}
    for number in intersectList :
        numberCountDic[number] = min(listX.count(number), listY.count(number))
    
    # key 기준으로 정렬해서 list로 반환.
    sortedNumbers = sorted(numberCountDic.items(), reverse=True)
    
    answer = ''
    for key, value in sortedNumbers :
        answer += str(key) * value
    
    return answer