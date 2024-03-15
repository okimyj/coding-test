def solution(n, lost, reserve):
    # 가져온 애가 도난 당했을 수 있다. lost, reserve에 중복되는 값은 제거한다.
    filteredLost = list(filter(lambda x: x not in reserve, lost))
    filteredReserve = list(filter(lambda x: x not in lost, reserve))
    
    def borrowUniform(number) :
        if number in filteredReserve :
            filteredReserve.remove(number)
            return True
        return False
    
    # 우선 체육복을 잃어버리지 않은 학생 수.
    answer = n-len(filteredLost)
    filteredLost.sort()         # 잃어버린 학생 번호순으로 정렬 

    for number in filteredLost :
        if borrowUniform(number-1) or borrowUniform(number+1) :
            answer +=1
            continue    
    return answer