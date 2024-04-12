'''
https://www.acmicpc.net/problem/1261
알고스팟
다익스트라 알고리즘.
해당 지점까지 가는데 부숴야하는 벽의 갯수를 우선순위 큐에 넣으면서..
'''
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().rstrip().split())
_map = [list(input().rstrip()) for _ in range(M)]
costMap = [[N*M]*N for _ in range(M)]
costMap[0][0] = 0
pq = []
heappush(pq, (costMap[0][0], 0, 0))

def isInRange(r, c):
    return r >= 0 and r < M and c >= 0 and c < N

while pq :
    cost, r, c = heappop(pq)
    for i in range(4) :
        nextR = r+dr[i]
        nextC = c+dc[i]

        if isInRange(nextR, nextC) :
            nextCost = cost + int(_map[nextR][nextC])
            if nextCost < costMap[nextR][nextC] :
                costMap[nextR][nextC] = nextCost
                heappush(pq, (nextCost, nextR, nextC))

print(costMap[M-1][N-1])