def solution(lottos, win_nums):
    matchedNum = 0
    zeroNum = 0
    for num in lottos :
        if num in win_nums :
            matchedNum += 1
        if num == 0 :
            zeroNum += 1
    answer = [min(6, 7-matchedNum-zeroNum), min(6, 7-matchedNum)]
    return answer