def solution(t, p):
    answer = 0
    pLen = len(p)
    num_p = int(p)
    for i in range(len(t)-pLen+1) : 
        split_num = int(t[i:i+pLen])
        if split_num <= num_p:
            answer+=1
    return answer