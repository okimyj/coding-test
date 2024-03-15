def solution(s):
    # 카운팅 변수 초기화, 첫번째 문자 변수 선언.
    count1 = 0
    count2 = 0
    firstChar = ""
    answer = 0
    
    for i in range(len(s)) :
        # firstChar이 빈문자열이면 현재 문자열 대입, count1++, answer++
        if firstChar == "" :
            firstChar = s[i]
            answer+=1
        if s[i] == firstChar :
            count1 += 1
        else :
            count2 += 1
            
        # count1과 count2가 같아지면 다시 초기화.
        if count1 == count2 :
            firstChar = ""
            count1=0
            count2=0
            
    
    return answer