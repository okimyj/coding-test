'''
https://www.acmicpc.net/problem/4485
녹색 옷 입은 애가 젤다지?
'''
import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def isInRange(mapSize, r, c) :
    return r >= 0 and r < mapSize and c >= 0 and c < mapSize

def getCost(mapSize) :
    _map = [list(map(int, input().rstrip().split())) for _ in range(mapSize)]
    _costMap = [[10*mapSize]*mapSize for _ in range(mapSize)]
    visited = [[False] * mapSize for _ in range(mapSize)]

    _costMap[0][0] = _map[0][0]
    q = deque([(0, 0, _map[0][0])])
    pq = []
    heappush(pq, (_map[0][0], 0, 0))
    while pq :
        curCost, curR, curC = heappop(pq)
        if curR == mapSize-1 and curC == mapSize-1 :
            break
        for i in range(4) :
            nextR = curR + dr[i]
            nextC = curC + dc[i]
            if isInRange(mapSize, nextR, nextC) and not visited[nextR][nextC] :
                if _costMap[nextR][nextC] > curCost + _map[nextR][nextC] :
                    _costMap[nextR][nextC] = min(_costMap[nextR][nextC], curCost + _map[nextR][nextC])
                    heappush(pq, (_costMap[nextR][nextC], nextR, nextC))

    # while q :
    #     curR, curC, curCost = q.popleft()
    #     # visited[curR][curC] = True
    #     for i in range(4) :
    #         nextR = curR + dr[i]
    #         nextC = curC + dc[i]
    #         if isInRange(mapSize, nextR, nextC) and not visited[nextR][nextC] :
    #             if _costMap[nextR][nextC] > curCost + _map[nextR][nextC] :
    #                 _costMap[nextR][nextC] = min(_costMap[nextR][nextC], curCost + _map[nextR][nextC])
    #                 q.append((nextR, nextC, _costMap[nextR][nextC]))

    return _costMap[mapSize-1][mapSize-1]

testNum = 0
while True :
    mapSize = int(input())
    if mapSize == 0:
        break
    testNum +=1
    print(f"Problem {testNum}: {getCost(mapSize)}")