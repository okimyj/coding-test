def solution(s):
    slen = len(s)
    
    return (slen == 4 or slen == 6) and s.isdigit()