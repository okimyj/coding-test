def solution(s):
    count1 = 0
    count2 = 0
    firstChar = s[0]
    answer = 1
    for i in range(len(s)-1) :
        if s[i] == firstChar :
            count1 += 1
        else :
            count2 += 1
        if count1 == count2 :
            firstChar = s[i+1]
            count1=0
            count2=0
            answer+=1
            
    
    return answer