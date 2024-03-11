def solution(x):
    xSum = sum(list(map(int, str(x))))
    
    return x % xSum == 0