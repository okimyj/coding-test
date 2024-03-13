def solution(num):
    MAX_TRY = 500
    i=0
    for i in range(MAX_TRY+1):
        if num == 1:
            break;
        num = num%2 == 0 and num/2 or num*3+1
    
    
    return i == MAX_TRY and -1 or i