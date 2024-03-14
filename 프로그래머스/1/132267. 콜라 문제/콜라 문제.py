# a병 당 b개의 콜라를 받음
# 상빈이가 가진 병 수 n
# a -> needNum
# b -> traceNum
# n -> hasNum
import math
def solution(needNum, traceNum, hasNum):
    answer = 0
    # 가지고 있는 병 수가 마트에서 콜라랑 바꿔주는 병 수보다 크거나 같은 동안 반복.
    while needNum <= hasNum :
        # 지금 가지고 있는 병 수로 바꿔서 받은 병 수 
        received = math.floor(hasNum/needNum) * traceNum
        # 가지고 있던 병 수를 필요한 병 수로 나눈 나머지에 바꿔서 받은 병을 더해 줌
        hasNum = hasNum % needNum + received;
        # 받은 콜라 +
        answer += received;
    
    return answer