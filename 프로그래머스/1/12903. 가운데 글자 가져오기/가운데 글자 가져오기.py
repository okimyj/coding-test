import math
def solution(s):
    midIndex = math.floor(len(s)/2)
    return len(s)%2 == 0 and s[midIndex-1:midIndex+1] or s[midIndex]