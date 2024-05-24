def solution(n):
    answer = []
    line = [0] * n
    for i in range(n) :
        answer.append(line.copy());
        answer[i][i] = 1
    return answer