def solution(s):
    answer = ''
    str_idx = 0
    # 0 부터 문자열 s의 길이 까지 반복.
    # 공백을 기준으로 단어가 구분된다. 공백을 만나면 index를 리셋 해주어야한다.
    for i in range(len(s)) :
        answer+= str_idx%2 == 0 and s[i].upper() or s[i].lower()
        str_idx+=1
        if s[i] == ' ' :
            str_idx=0
        
    return answer