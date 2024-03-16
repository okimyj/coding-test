def solution(park, routes):
    # [row, col]
    MOVE_OPERATION = {'N':[-1,0], 'E':[0,1], 'S':[1, 0], 'W':[0,-1]}
    
    curRow = None
    curCol = None
    parkMap = []
    # parkMap 만들면서 start위치 찾기.
    for i, load in enumerate(park) :
        parkMap.append(list(load))
        if not curCol :
            index = load.find('S')
            if index != -1 :
                curCol = index
                curRow = i
    rows = len(parkMap)
    cols = len(parkMap[0])
    # print("rows : " , rows, " cols : ", cols)
    # print("start : " , curRow, ", ", curCol)
    
    def isInRange(r, c) :
        return r >= 0 and r < rows and c >= 0 and c < cols
    
    for command in routes :
        op, unit = command.split(' ')
        dir = MOVE_OPERATION[op]
        newRow = curRow + dir[0] * int(unit)
        newCol = curCol + dir[1] * int(unit)
        # print("-- dir : " , dir, " unit : " , unit)
        if isInRange(newRow, newCol) :
            canMove = True
            # 이동 경로 중 장애물이 있는지 확인
            if dir[0] != 0 :
                # print("curRow : ", curRow, "newRow : ", newRow)
                for row in range(curRow, newRow+dir[0], dir[0]) :
                    if parkMap[row][curCol] == 'X' :
                        canMove = False
                        break
            if dir[1] != 0 :
                # print("curCol : ", curCol, "newCol : ", newCol)
                for col in range(curCol, newCol+dir[1], dir[1]) :
                    # print("col : " , col , " parkMap[curRow][col] : " , parkMap[curRow][col])
                    if parkMap[curRow][col] == 'X' :
                        canMove = False
                        break
                
            if canMove :
                curRow = newRow
                curCol = newCol
        
    
                
    
    answer = [curRow, curCol]
    return answer