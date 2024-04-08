'''
https://www.acmicpc.net/problem/10026
적록색약
- dfs
- R, G 는 RG로 visited 표시 -> 최종은 0
-
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
countDict = defaultdict(int)
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visitedA = [[False] * N for _ in range(N)]
visitedB = [[False] * N for _ in range(N)]
def isInRange(r, c) :
    return r >= 0 and r < N and c >= 0 and c < N
def canVisit(r, c, isCheckRG) :
    if not isInRange(r, c) :
        return False
    if isCheckRG :
        return graph[r][c] == 'RG'
    else:
        return graph[r][c] in ['R','G','B']
def setVisit(r, c) :
    if graph[r][c] == 'R' or graph[r][c] == 'G' :
        graph[r][c] = 'RG'
    else :
        graph[r][c] = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c, checkC, isCheckRG) :
    q = deque([(r, c)])
    while q :
        curR, curC = q.popleft()
        for i in range(4):
            nextR = curR + dr[i]
            nextC = curC + dc[i]
            if canVisit(nextR, nextC, isCheckRG) and graph[nextR][nextC] == checkC:
                setVisit(nextR, nextC)
                q.append((nextR,nextC))
# def dfs(r, c, checkC, isCheckRG) :
#     for i in range(4) :
#         nextR = r + dr[i]
#         nextC = c + dc[i]
#         if canVisit(nextR, nextC,isCheckRG) and graph[nextR][nextC] == checkC:
#             setVisit(nextR, nextC)
#             dfs(nextR, nextC, checkC, isCheckRG)

def checkCount(isCheckRG) :
    for r in range(N) :
        for c in range(N) :
            if canVisit(r, c, isCheckRG) :
                checkC = graph[r][c]
                countDict[checkC] += 1
                setVisit(r, c)
                bfs(r, c, checkC, isCheckRG)

checkCount(False)
checkCount(True)
print(countDict['R']+countDict['G']+countDict['B'], countDict['RG']+countDict['B'], sep=' ')
