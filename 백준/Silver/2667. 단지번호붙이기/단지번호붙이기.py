import sys
from collections import deque, defaultdict
input = sys.stdin.readline
mapSize = int(input())
_map = [list(input().rstrip()) for x in range(mapSize)]
def isInRange(r, c) :
    return r >= 0 and r < mapSize and c >= 0 and c < mapSize
def canVisit(r, c) :
    return isInRange(r, c) and _map[r][c] == '1' and not visited[r][c]

visited = [[False for _ in range(mapSize)] for _ in range(mapSize)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
areaNum = []
areaIdx = -1
def bfs(r, c) :
    q = deque([(r,c)])
    visited[r][c] = areaNum

    while q :
        curR, curC = q.popleft()
        for i in range(4) :
            nextR = curR + dr[i]
            nextC = curC + dc[i]
            # r, c 가 범위 내에 있고, _map의 r, c의 값이 1이고 방문하지 않은 곳이라면 append.
            if canVisit(nextR, nextC) :
                q.append((nextR, nextC))
                visited[nextR][nextC] = True
                areaNum[areaIdx] += 1

for r in range(mapSize) :
    for c in range(mapSize) :
        if canVisit(r, c) :
            areaNum.append(1)
            areaIdx += 1
            bfs(r, c)

print(len(areaNum))
areaNum.sort()
print(*areaNum, sep="\n")