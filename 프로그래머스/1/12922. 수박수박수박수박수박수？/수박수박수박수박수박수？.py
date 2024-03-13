import math
def solution(n):
    PATTERN_KEY = "수박"
    answer = PATTERN_KEY * math.ceil(n/2)
    if n % 2 != 0 :
        answer = answer[0:-1]
    return answer