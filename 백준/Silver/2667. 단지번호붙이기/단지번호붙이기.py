# 단지 번호 붙이기
import sys
from collections import deque
input = sys.stdin.readline
inputMap = []
mapSize = int(input())
visited = [[0 for _ in range(mapSize)] for _ in range(mapSize)]
areaNum = []
for i in range(mapSize) :
    inputMap.append(list(input().rstrip()))

def isInRange(r, c) :
   return r >= 0 and r < mapSize and c >= 0 and c < mapSize

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(r, c):
    areaNum[len(areaNum)-1] += 1
    visited[r][c] = True
    q = deque()
    q.append((r, c))
    while q :
        curR, curC = q.popleft()
        for i in range(4) :
            nextR = curR + dr[i]
            nextC = curC + dc[i]
            if isInRange(nextR, nextC) and not visited[nextR][nextC] and inputMap[nextR][nextC] == '1' :
                areaNum[len(areaNum) - 1] += 1
                visited[nextR][nextC] = True
                q.append((nextR, nextC))

for i in range(mapSize) :
    for j in range(mapSize):
        if isInRange(i, j) and not visited[i][j] and inputMap[i][j] == '1':
            areaNum.append(0)
            bfs(i, j)

areaNum.sort()
print(len(areaNum))
for i in areaNum :
    print(i)