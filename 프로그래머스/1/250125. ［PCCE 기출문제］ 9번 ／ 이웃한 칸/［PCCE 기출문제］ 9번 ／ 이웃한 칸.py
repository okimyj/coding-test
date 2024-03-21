def solution(board, h, w):
    answer = 0
    rows = len(board)
    cols = len(board[0])
    def isInRange (r, c) :
        return r >= 0 and r < rows and c >= 0 and c < cols
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    checkColor = board[h][w]
    for d in dir :
        checkR = h+d[0]
        checkC = w+d[1]
        if isInRange(checkR, checkC) and board[checkR][checkC] == checkColor:
            answer += 1

    return answer