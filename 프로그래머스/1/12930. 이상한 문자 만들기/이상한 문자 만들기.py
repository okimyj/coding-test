def solution(s):
    answer = ''
    str_idx = 0
    for i in range(len(s)) :
        answer+= str_idx%2 == 0 and s[i].upper() or s[i].lower()
        str_idx+=1
        if s[i] == ' ' :
            str_idx=0
        
    return answer