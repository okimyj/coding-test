'''
https://www.acmicpc.net/problem/4485
녹색 옷 입은 애가 젤다지?
다익스트라 알고리즘 사용.
map 에 대응되는 costMap 을 생성.
처음에는 최대 값으로 채워주고, 현재 cost + map에 있는 cost 중 적은 비용으로 갱신.
비용이 더 적은 경우에만 우선순위 큐에 push 하고 비용 적은순으로 pop.
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def isInRange(mapSize, r, c) :
    return r >= 0 and r < mapSize and c >= 0 and c < mapSize

def getCost(mapSize) :
    _map = [list(map(int, input().rstrip().split())) for _ in range(mapSize)]
    _costMap = [[10*mapSize]*mapSize for _ in range(mapSize)]
    _costMap[0][0] = _map[0][0]
    pq = []
    heappush(pq, (_map[0][0], 0, 0))
    while pq :
        curCost, curR, curC = heappop(pq)
        for i in range(4) :
            nextR = curR + dr[i]
            nextC = curC + dc[i]
            if isInRange(mapSize, nextR, nextC) :
                nextCost = curCost + _map[nextR][nextC] 
                if nextCost < _costMap[nextR][nextC] :
                    _costMap[nextR][nextC] = nextCost
                    heappush(pq, (nextCost, nextR, nextC))
    # deque 사용 시간 초과..
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


# 메모리 초과..
# def getCost(mapSize) :
#     _map = [list(map(int, input().rstrip().split())) for _ in range(mapSize)]
#     visited = [[False] * mapSize for _ in range(mapSize)]
#     def dfs(r, c, curCost) :
#         if r == mapSize-1 and c == mapSize -1 :
#             return curCost
#         nextR = 0
#         nextC = 0
#         minCost = 10
#         for i in range(4) :
#             tempR = r + dr[i]
#             tempC = c + dc[i]
#
#             if isInRange(mapSize, tempR, tempC) and not visited[tempR][tempC] :
#                 if tempR == mapSize-1 and tempC == mapSize -1 :
#                     minCost = _map[tempR][tempC]
#                     nextR = tempR
#                     nextC = tempC
#                     break
#                 if _map[tempR][tempC] < minCost :
#                     minCost = _map[tempR][tempC]
#                     nextR = tempR
#                     nextC = tempC
#
#         visited[nextR][nextC] = True
#         return dfs(nextR, nextC, curCost + minCost)
#
#     visited[0][0] = True
#     return dfs(0, 0, _map[0][0])